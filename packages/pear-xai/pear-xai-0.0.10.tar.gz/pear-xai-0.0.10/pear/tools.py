"""
tools.py
Helper functions
"""
import logging
import os

import pandas as pd
import torch
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from torch.utils.data import DataLoader


class TabularDataLoader(torch.utils.data.Dataset):
    def __init__(self, path, filename, label, scale="minmax"):

        self.path = path
        self.dataset = pd.read_csv(path + filename)
        self.target = label
        self.X = self.dataset.drop(self.target, axis=1)
        self.feature_names = self.X.columns.to_list()
        self.target_name = label
        if scale == 'minmax':
            self.scaler = MinMaxScaler()
        elif scale == 'standard':
            self.scaler = StandardScaler()
        else:
            raise NotImplementedError("only minmax, standard scaling")

        self.scaler.fit_transform(self.X)
        self.data = self.scaler.transform(self.X)
        self.targets = self.dataset[self.target]

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):

        # select correct row with idx
        if isinstance(idx, torch.Tensor):
            idx = idx.tolist()
        return self.data[idx], self.targets.values[idx]


def get_data(dataset: str, batch_size: int, data_path="./datasets"):
    """
    Helper function to get data-loaders for different datasets
    """
    if dataset in ["bankmarketing", "californiahousing", "electricity"]:
        dataset_train = TabularDataLoader(path=f"{data_path}/{dataset}/",
                                          filename=f"{dataset}-train.csv",
                                          label="class")

        dataset_test = TabularDataLoader(path=f"{data_path}/{dataset}/",
                                         filename=f"{dataset}-test.csv",
                                         label="class")

        loader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
        loader_test = DataLoader(dataset_test, batch_size=batch_size, shuffle=True)
        num_classes = 2
    elif dataset in ["corrupt-bankmarketing", "corrupt-californiahousing", "corrupt-electricity"]:
        dataset_train = TabularDataLoader(path=f"{data_path}/{dataset[8:]}/",
                                          filename=f"{dataset[8:]}-train.csv",
                                          label="class")

        dataset_test = TabularDataLoader(path=f"{data_path}/{dataset[8:]}/",
                                         filename=f"{dataset[8:]}-test.csv",
                                         label="class")
        dataset_train.data = torch.tensor(dataset_train.data)
        dataset_test.data = torch.tensor(dataset_test.data)
        dataset_train.data = torch.concat([dataset_train.data,
                                           torch.rand_like(dataset_train.data)], dim=1)
        dataset_test.data = torch.concat([dataset_test.data,
                                          torch.rand_like(dataset_test.data)], dim=1)
        loader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
        loader_test = DataLoader(dataset_test, batch_size=batch_size, shuffle=True)
        num_classes = 2
    else:
        raise ValueError(f"The dataset name {dataset} is not yet available in this repo.")

    return loader_train, loader_test, num_classes


def save_model(model, explainers, disagreement_lambda, disagreement_mu, dest):
    """
    Helper function to save the torch model to disk
    """
    logging.info(f"Saving checkpoint to {os.path.join(os.getcwd(), dest)}...")
    state_dict = {"model": model.state_dict(),
                  "explainers": explainers,
                  "lambda": disagreement_lambda,
                  "mu": disagreement_mu}
    torch.save(state_dict, dest)
