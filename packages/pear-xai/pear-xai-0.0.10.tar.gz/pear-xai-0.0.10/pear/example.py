"""
example.py
A example script showing how to train and save neural nets with PEAR.
"""

import logging
import os
from pathlib import Path

import torch
from torch.optim import SGD, Adam, AdamW

import pear


def run_example():
    logging.basicConfig(level=logging.INFO,
                        format="[%(asctime)s %(levelname)s]: %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S")
    logging.info("\n_________________________________________________\n")
    logging.info("example.py main() running.")

    ##############################################
    # Set up -- experiment control constants
    ##############################################

    dataset = "californiahousing"
    batch_size = 64
    model_cfg = {"name": "mlp",
                 "width": 100,
                 "depth": 3}
    optimizer = "adamw"
    lr = 5e-3
    weight_decay = 2e-4
    explainers = ["vanilla_gradients", "integrated_gradients"]
    disagreement_lambda = 0.25
    disagreement_mu = 0.5
    epochs = 3
    ##############################################

    # Get data
    here = Path(__file__).parent
    loader_train, loader_test, num_classes = pear.get_data(dataset, batch_size, data_path=os.path.join(here, "datasets/"))
    input_dim = loader_train.dataset.data.shape[1]
    num_training_data = loader_train.dataset.data.shape[0]
    num_testing_data = loader_test.dataset.data.shape[0]
    logging.info(f"{dataset} dataset with {num_training_data} training samples and {num_testing_data} testing samples"
                 f" and {input_dim} features and "
                 f"{torch.unique(torch.tensor(loader_train.dataset.targets), return_counts=True)} classes.")

    # Create a model
    model = pear.get_model(model_cfg, input_dim, num_classes)
    pytorch_total_params = sum(p.numel() for p in model.parameters())
    logging.info(f"This {model_cfg['name']} has {pytorch_total_params / 1e3:0.3f} thousand parameters.")

    # Get an optimizer
    params = model.parameters()
    if optimizer == "sgd":
        optim = SGD(params, lr=lr, weight_decay=weight_decay, momentum=0.9)
    elif optimizer == "adam":
        optim = Adam(params, lr=lr, weight_decay=weight_decay)
    elif optimizer == "adamw":
        optim = AdamW(params, lr=lr, weight_decay=weight_decay)

    # Create two explainers
    explainer_a = pear.get_explainer(explainers[0], model, torch.tensor(loader_train.dataset.data))
    explainer_b = pear.get_explainer(explainers[1], model, torch.tensor(loader_train.dataset.data))
    lime = pear.get_explainer("lime", model, torch.tensor(loader_train.dataset.data))
    shap = pear.get_explainer("shap", model, torch.tensor(loader_train.dataset.data))

    # get a metric and define a loss function
    disagreement_loss_fn = pear.DisagreementLoss(explainer_a, explainer_b, disagreement_mu)

    # Training loop
    for epoch in range(epochs):
        _ = model.train_loop(trainloader=loader_train,
                             disagreement_lambda=disagreement_lambda,
                             optimizer=optim,
                             task_loss_fn=torch.nn.CrossEntropyLoss(),
                             disagreement_loss_fn=disagreement_loss_fn)
        evaluation_on_train_data = model.evaluate_balanced(loader_train,
                                                           task_loss_fn=torch.nn.CrossEntropyLoss(),
                                                           disagreement_loss_fn=disagreement_loss_fn)
        evaluation_on_test_data = model.evaluate_balanced(loader_test,
                                                          task_loss_fn=torch.nn.CrossEntropyLoss(),
                                                          disagreement_loss_fn=disagreement_loss_fn)

        logging.info(f"epoch {epoch:2d} | "
                     f"task loss {evaluation_on_train_data['task_loss']:.4f} | "
                     f"disagree loss {evaluation_on_train_data['disagreement_loss']:.4f} | "
                     f"train bal acc {(evaluation_on_train_data['acc_0'] + evaluation_on_train_data['acc_1']) / 2:.2f} | "
                     f"test bal acc {(evaluation_on_test_data['acc_0'] + evaluation_on_test_data['acc_1']) / 2:.2f} | "
                     )

        disagreement_vals = pear.get_disagreement_values(loader_train, explainer_a, explainer_b, disagreement_k=5)
        eval_str = f""
        for k in disagreement_vals.keys():
            eval_str += f"{k}: {disagreement_vals[k]:.4f} | "
        logging.info(eval_str)

        disagreement_vals = pear.get_disagreement_values(loader_test, explainer_a, explainer_b, disagreement_k=5)
        eval_str = f""
        for k in disagreement_vals.keys():
            eval_str += f"{k}: {disagreement_vals[k]:.4f} | "
        logging.info(eval_str)

    # Save final model
    pear.save_model(model, explainers, disagreement_lambda, disagreement_mu, "final_checkpoint.pth")

    # Save the results from this training run
    result = {"model": model_cfg["name"],
              "dataset": dataset,
              "task_loss_test_data": evaluation_on_test_data['task_loss'],
              "disagreement_loss_test_data": evaluation_on_test_data['disagreement_loss'],
              "task_loss_train_data": evaluation_on_train_data['task_loss'],
              "disagreement_loss_train_data": evaluation_on_train_data['disagreement_loss'],
              "train_acc": evaluation_on_train_data['acc'],
              "test_acc": evaluation_on_test_data['acc'],
              }

    logging.info("Done.")


if __name__ == "__main__":
    run_example()
