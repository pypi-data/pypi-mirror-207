"""
disagreement_loss.py
disagreement loss fucntions.
"""

import torch

from fast_soft_sort import pytorch_ops
from .explainers import Explainer


def pearson(raw_feature_scores_a: torch.Tensor, raw_feature_scores_b: torch.Tensor, reduction="mean") -> float:
    """
    Function to compute pearson correlation between two vectors
    :param raw_feature_scores_a: feature importance scores a
    :param raw_feature_scores_b: feature importance scores b
    :param reduction: method to reduce the vector to a value (mean)
    :return:
    """
    scores_a = raw_feature_scores_a - raw_feature_scores_a.mean(dim=1).unsqueeze(1)
    scores_a = scores_a / scores_a.norm(dim=1).unsqueeze(1)

    scores_b = raw_feature_scores_b - raw_feature_scores_b.mean(dim=1).unsqueeze(1)
    scores_b = scores_b / scores_b.norm(dim=1).unsqueeze(1)

    pearson_rho = (scores_a * scores_b).sum(dim=1)
    if reduction == "mean":
        pearson_rho = pearson_rho.mean()

    return pearson_rho


def soft_spearman(raw_feature_scores_a: torch.Tensor, raw_feature_scores_b: torch.Tensor, reduction="mean") -> float:
    """
    Function to compute approximate spearman using fast_soft_sort ranking
    :param raw_feature_scores_a: feature important scores a
    :param raw_feature_scores_b: feature important scores b
    :param reduction: method to reduce output vector
    :return:
    """
    scores_a = torch.abs(raw_feature_scores_a)
    rank_a = pytorch_ops.soft_rank(scores_a, regularization_strength=0.2)
    rank_a = rank_a - rank_a.mean(dim=1).unsqueeze(1)
    rank_a = rank_a / rank_a.norm(dim=1).unsqueeze(1)

    scores_b = torch.abs(raw_feature_scores_b)
    rank_b = pytorch_ops.soft_rank(scores_b, regularization_strength=0.2)
    rank_b = rank_b - rank_b.mean(dim=1).unsqueeze(1)
    rank_b = rank_b / rank_b.norm(dim=1).unsqueeze(1)

    out = (rank_a * rank_b).sum(dim=1)
    if reduction == "mean":
        out = out.mean()

    return out


class DisagreementLoss(torch.nn.Module):
    def __init__(self, explainer_a: Explainer, explainer_b: Explainer, mu: float):
        """
        Build generalizable disagreement loss torch module
        :param explainer_a: explainer object to compute explanations
        :param explainer_b: explainer object to compute explanations
        :param mu: weight of the loss
        """
        super(DisagreementLoss, self).__init__()
        self.explainer1 = explainer_a
        self.explainer2 = explainer_b
        self.mu = mu

    def forward(self, inputs, labels):
        feature_scores_one = self.explainer1.get_explanation(inputs, labels)
        feature_scores_two = self.explainer2.get_explanation(inputs, labels)
        metric_loss = (1 - soft_spearman(feature_scores_one, feature_scores_two)) / 2
        pearson_loss = (1 - pearson(feature_scores_one, feature_scores_two)) / 2
        return self.mu * metric_loss + (1 - self.mu) * pearson_loss
