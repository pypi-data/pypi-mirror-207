"""
models.py
A collection of neural network model classes and functions.
"""

from typing import List, Optional

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import accuracy_score
from torch.utils.data import DataLoader
from tqdm import tqdm

from .disagreement_loss import DisagreementLoss


class Model(nn.Module):
    def __init__(self):
        super().__init__()

    def train_loop(self,
                   trainloader: DataLoader,
                   disagreement_lambda: float,
                   optimizer: torch.optim.Optimizer,
                   task_loss_fn: torch.nn.Module,
                   disagreement_loss_fn: DisagreementLoss) -> dict:
        """
        Run one epoch of a training loop for any dataloader
        :param trainloader: train data loader
        :param disagreement_lambda: lambda term for disagreement loss
        :param optimizer: torch optimizer
        :param task_loss_fn: loss function of the actual classification problem
        :param disagreement_loss_fn: disagreement loss function
        :return:
        """

        train_loss = 0.0
        task_loss_total = 0.0
        num_training_data = 0
        disagreement_loss_total = 0.0

        for inputs, targets in tqdm(trainloader, leave=False):
            optimizer.zero_grad()
            outputs = self.forward(inputs)
            task_loss = torch.tensor(0.0)
            disagreement_loss = torch.tensor(0.0)

            if disagreement_lambda > 0.0:
                disagreement_loss = disagreement_loss_fn(inputs, targets)
            if disagreement_lambda < 1.0:
                task_loss = task_loss_fn(outputs, targets)

            full_loss = (1 - disagreement_lambda) * task_loss + disagreement_lambda * disagreement_loss
            full_loss.backward()
            optimizer.step()

            train_loss += full_loss.detach() * targets.size(0)
            num_training_data += targets.size(0)
            task_loss_total += task_loss.detach() * targets.size(0)
            disagreement_loss_total += disagreement_loss.detach() * targets.size(0)

        results = {"task_loss": (task_loss_total / num_training_data).item(),
                   "disagreement_loss": (disagreement_loss_total / num_training_data).item()}

        return results

    def evaluate(self, dataloader: DataLoader, task_loss_fn: torch.nn.Module, disagreement_loss_fn: DisagreementLoss):
        correct = 0.0
        num_training_data = 0
        task_loss_total = 0.0
        disagreement_loss_total = 0.0
        for inputs, targets in tqdm(dataloader, leave=False):
            outputs = self.forward(inputs)
            yhat = torch.argmax(outputs, dim=1).detach().numpy()
            correct += accuracy_score(yhat, targets.detach().numpy(), normalize=False)
            num_training_data += targets.size(0)
            disagreement_loss = disagreement_loss_fn(inputs, targets)
            task_loss = task_loss_fn(outputs, targets)
            task_loss_total += task_loss.detach() * targets.size(0)
            disagreement_loss_total += disagreement_loss.detach() * targets.size(0)

        result = {"acc": 100.0 * correct / num_training_data,
                  "task_loss": (task_loss_total / num_training_data).item(),
                  "disagreement_loss": (disagreement_loss_total / num_training_data).item()}
        return result

    def evaluate_balanced(self, dataloader: DataLoader, task_loss_fn: torch.nn.Module,
                          disagreement_loss_fn: DisagreementLoss):
        correct_in_class_0 = 0.0
        correct_in_class_1 = 0.0
        correct = 0.0
        num_training_data = 0
        num_training_data_0 = 0
        num_training_data_1 = 0
        task_loss_total = 0.0
        disagreement_loss_total = 0.0
        for inputs, targets in tqdm(dataloader, leave=False):
            outputs = self.forward(inputs)
            yhat = torch.argmax(outputs, dim=1).detach().numpy()
            correct += accuracy_score(yhat, targets.detach().numpy(), normalize=False)
            correct_in_class_0 += accuracy_score(yhat[targets == 0], targets[targets == 0].detach().numpy(),
                                                 normalize=False)
            correct_in_class_1 += accuracy_score(yhat[targets == 1], targets[targets == 1].detach().numpy(),
                                                 normalize=False)
            num_training_data += targets.size(0)
            num_training_data_0 += targets[targets == 0].size(0)
            num_training_data_1 += targets[targets == 1].size(0)
            disagreement_loss = disagreement_loss_fn(inputs, targets)
            task_loss = task_loss_fn(outputs, targets)
            task_loss_total += task_loss.detach() * targets.size(0)
            disagreement_loss_total += disagreement_loss.detach() * targets.size(0)

        result = {"acc": 100.0 * correct / num_training_data,
                  "acc_0": 100.0 * correct_in_class_0 / (num_training_data_0 + 1e-4),
                  "acc_1": 100.0 * correct_in_class_1 / (num_training_data_1 + 1e-4),
                  "task_loss": (task_loss_total / num_training_data).item(),
                  "disagreement_loss": (disagreement_loss_total / num_training_data).item()}
        return result


class MLP(Model):
    def __init__(self,
                 input_dim: int,
                 num_classes: int,
                 hidden_layers: List[int] = [100],
                 activation_fns: Optional[List[nn.modules.Module]] = None):
        """
        General class to define ANN with an arbitrary amount of layers and activation functions

        :param input_dim: number of input features
        :param num_classes: number of prediction classes
        :param hidden_layers: list of integers representing number of neurons per hidden layer
        :param activation_fns: list of activation fns for each hidden layer (defaults to ReLU)
        """
        super().__init__()
        # Error checking for activation functions
        if activation_fns:
            assert len(activation_fns) == len(hidden_layers), "You must specify activation functions for each layer"

        else:
            activation_fns = [nn.ReLU() for _ in range(len(hidden_layers))]

        # make the model, layer by layer
        layers = []

        hidden_layers.insert(0, input_dim)
        hidden_layers.append(num_classes)

        for i in range(len(hidden_layers) - 1):
            layers.append(nn.Linear(hidden_layers[i], hidden_layers[i + 1]))

            # Make sure we don't add activation function to our output layer
            if i < len(activation_fns):
                layers.append(activation_fns[i])
        self.layers = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor):
        """
        Run feed forward for the defined neural net (note output class weights are NOT normalized)

        :param x: input batch
        """
        if x.dtype is not torch.float:
            x = x.float()

        return self.layers(x)

    def predict_proba(self, x: torch.Tensor) -> np.ndarray:
        """
        Return the predicted class probabilities through a softmax layer

        :param x: input batch
        """
        if x.dtype is not torch.float:
            x = x.float()

        out = F.softmax(self.forward(x), dim=1)

        return out.detach().numpy()

    def predict(self, x: torch.Tensor) -> np.ndarray:
        """
        Return the class label for the inputs

        :param x: input batch
        """
        out = self.forward(x)
        normalized = F.softmax(out, dim=1)

        return torch.argmax(normalized, dim=1).detach().numpy()


class Linear(Model):
    def __init__(self, input_dim: int, num_classes: int):
        """
        General class to define ANN with an arbitrary amount of layers and activation functions

        :param input_dim: number of input features
        :param num_classes: number of prediction classes
        :param hidden_layers: list of integers representing number of neurons per hidden layer
        :param activation_fns: list of activation fns for each hidden layer (defaults to ReLU)
        """
        super().__init__()
        self.model = nn.Linear(input_dim, num_classes)

    def forward(self, x: torch.Tensor):
        """
        Run feed forward for the defined neural net (note output class weights are NOT normalized)

        :param x: input batch
        """
        if x.dtype is not torch.float:
            x = x.float()

        return self.model(x)

    def predict_proba(self, x: torch.Tensor) -> np.ndarray:
        """
        Return the predicted class probabilities through a softmax layer

        :param x: input batch
        """
        if x.dtype is not torch.float:
            x = x.float()

        out = F.softmax(self.forward(x), dim=1)

        return out.detach().numpy()

    def predict(self, x: torch.Tensor) -> np.ndarray:
        """
        Return the class label for the inputs

        :param x: input batch
        """
        out = self.forward(x)
        normalized = F.softmax(out, dim=1)

        return torch.argmax(normalized, dim=1).detach().numpy()


def get_model(model_cfg: dict, input_dim: int, num_classes: int) -> nn.Module:
    if model_cfg["name"] == "mlp":
        return MLP(input_dim, num_classes, [model_cfg["width"]] * model_cfg["depth"])
    elif model_cfg["name"] == "linear":
        return Linear(input_dim, num_classes)
    else:
        raise ValueError(f"Model {model_cfg['name']} not yet implemented.")
