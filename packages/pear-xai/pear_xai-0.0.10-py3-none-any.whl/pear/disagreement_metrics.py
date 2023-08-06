"""
disagreement_metrics.py
disagreement evaluation fucntions.
"""

import itertools
from typing import Tuple

import numpy as np
import torch
from scipy.special import comb
from scipy.stats import rankdata, pearsonr

from .explainers import get_explainer


def get_top_k_features(raw_feature_scores_a: torch.Tensor,
                       raw_feature_scores_b: torch.Tensor,
                       k: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return the top k features for both set of explanations
    """
    # id of top-k features
    topk_explainer_a = np.argsort(-np.abs(raw_feature_scores_a.detach().numpy()), axis=1)[:, 0:k]
    topk_explainer_b = np.argsort(-np.abs(raw_feature_scores_b.detach().numpy()), axis=1)[:, 0:k]

    return topk_explainer_a, topk_explainer_b


def feature_agreement(raw_feature_scores_a: torch.Tensor,
                      raw_feature_scores_b: torch.Tensor,
                      k: int,
                      reduction="mean") -> float:
    """
    Returns the feature agreement for the two set of explanations
    """
    # id of top-k features
    topk_explainer_a, topk_explainer_b = get_top_k_features(raw_feature_scores_a.clone(), raw_feature_scores_b.clone(),
                                                            k)
    # calculate individual intersection and average using some numpy magic
    stack = np.hstack((topk_explainer_a, topk_explainer_b))
    stack.sort(axis=1)
    intersection_scores = np.sum(stack[:, 1:] == stack[:, :-1], axis=1) / k

    if reduction == "mean":
        output = intersection_scores.mean()
    elif reduction is None:
        output = intersection_scores
    else:
        raise NameError(f"reduction should be one of {{'mean', None}}, got {reduction} instead.")

    return output


def rank_agreement(raw_feature_scores_a: torch.Tensor,
                   raw_feature_scores_b: torch.Tensor,
                   k: int,
                   reduction="mean") -> float:
    """
    Return the rank agreement for the two set of explanations

    """
    # id of top-k features
    topk_explainer_a, topk_explainer_b = get_top_k_features(raw_feature_scores_a.clone(), raw_feature_scores_b.clone(),
                                                            k)

    # calculate rank agreement
    rank_scores = (topk_explainer_a == topk_explainer_b).sum(axis=1) / k

    if reduction == "mean":
        output = rank_scores.mean()
    elif reduction is None:
        output = rank_scores
    else:
        raise NameError(f"reduction should be one of {{'mean', None}}, got {reduction} instead.")

    return output


def sign_agreement(raw_feature_scores_a: torch.Tensor,
                   raw_feature_scores_b: torch.Tensor,
                   k: int,
                   reduction="mean") -> float:
    """
    Return the sign agreemeent for the two set of explanations
    """
    # get the top-k features
    topk_explainer_a, topk_explainer_b = get_top_k_features(raw_feature_scores_a.clone(),
                                                            raw_feature_scores_b.clone(),
                                                            k)

    # get the sign intersections for the topk explainers
    output = []
    for i in range(len(topk_explainer_a)):
        explainer_a_indices = set(topk_explainer_a[i])
        explainer_b_indices = set(topk_explainer_b[i])
        intersection = explainer_a_indices.intersection(explainer_b_indices)
        sign_count = 0
        for val in intersection:
            sign_a = np.sign(raw_feature_scores_a.detach().numpy()[i][val])
            sign_b = np.sign(raw_feature_scores_b.detach().numpy()[i][val])
            if sign_a == sign_b:
                sign_count += 1
        # Add to output
        output.append(sign_count / k)

    output = np.array(output, dtype=np.float32)
    if reduction == "mean":
        output = output.mean()
    elif reduction is None:
        pass
    else:
        raise NameError(f"reduction should be one of {{'mean', None}}, got {reduction} instead.")

    return output


def signed_rank_agreement(raw_feature_scores_a: torch.Tensor,
                          raw_feature_scores_b: torch.Tensor,
                          k: int,
                          reduction="mean") -> float:
    """
    Return the sign ranked agreement for the two set of explanations
     """
    # get the top-k features
    topk_explainer_a, topk_explainer_b = get_top_k_features(raw_feature_scores_a.clone(),
                                                            raw_feature_scores_b.clone(),
                                                            k)

    # get the sign intersections for the topk explainers
    output = []
    for i in range(len(topk_explainer_a)):
        explainer_a_indices = topk_explainer_a[i]
        explainer_b_indices = topk_explainer_b[i]
        intersection = explainer_a_indices[np.where(explainer_a_indices == explainer_b_indices)[0]]
        signs_eq = np.sign(raw_feature_scores_a[i][intersection]) == np.sign(raw_feature_scores_b[i][intersection])

        # Add to output
        output.append(signs_eq.sum() / k)

    output = np.array(output, dtype=np.float32)
    if reduction == "mean":
        output = output.mean()
    elif reduction is None:
        pass
    else:
        raise NameError(f"reduction should be one of {{'mean', None}}, got {reduction} instead.")

    return output


def rank_correlation(raw_feature_scores_a: torch.Tensor,
                     raw_feature_scores_b: torch.Tensor,
                     k: int = None,
                     reduction="mean") -> float:
    """
    Returns the rank correlation for the two sets of explanations
    """
    ranks_a = rankdata(np.abs(raw_feature_scores_a.detach().numpy()), axis=1)
    ranks_b = rankdata(np.abs(raw_feature_scores_b.detach().numpy()), axis=1)

    num_samples = raw_feature_scores_a.shape[0]
    rho_array = np.zeros(num_samples)
    for i in range(num_samples):
        rho, _ = pearsonr(ranks_a[i], ranks_b[i])
        rho_array[i] = rho

    if reduction == "mean":
        output = rho_array.mean()
    elif reduction is None:
        output = rho_array
    else:
        raise NameError(f"reduction should be one of {{'mean', None}}, got {reduction} instead.")

    return output


def pairwise_rank_agreement(raw_scores_a: torch.Tensor,
                            raw_scores_b: torch.Tensor,
                            k: int = None) -> float:
    """
    Computes the pairwise rank agreement between two vectors

    :return:
    """
    scores_a = raw_scores_a.detach().numpy()
    scores_b = raw_scores_b.detach().numpy()
    n_datapoints = scores_a.shape[0]
    n_feat = scores_a.shape[1]
    # rank of all features --> manually calculate rankings (instead of using 0, 1, ..., k ranking based on argsort
    # output) to account for ties rankdata gives rank1 for smallest # --> we want rank1 for largest # (aka # with
    # largest magnitude)
    all_feat_ranks_a = rankdata(-np.abs(scores_a), method='dense', axis=1)
    all_feat_ranks_b = rankdata(-np.abs(scores_b), method='dense', axis=1)
    # count # of pairs of features with same relative ranking
    feat_pairs_w_same_rel_rankings = np.zeros(n_datapoints)
    for feat1, feat2 in itertools.combinations_with_replacement(range(n_feat), 2):
        if feat1 != feat2:
            rel_ranking_a = all_feat_ranks_a[:, feat1] < all_feat_ranks_a[:, feat2]
            rel_ranking_b = all_feat_ranks_b[:, feat1] < all_feat_ranks_b[:, feat2]
            feat_pairs_w_same_rel_rankings += rel_ranking_a == rel_ranking_b
    pairwise_distr = feat_pairs_w_same_rel_rankings / comb(n_feat, 2)
    return pairwise_distr.mean()


def get_disagreement_values(loader_test, explainer_a, explainer_b, disagreement_k):
    """
    Helper function to get all the evaluation metrics for a test loader
    """
    metrics_dict = {
        "feature_agreement": feature_agreement,
        "rank_agreement": rank_agreement,
        "sign_agreement": sign_agreement,
        "signed_rank_agreement": signed_rank_agreement,
        "rank_correlation": rank_correlation,
        "pairwise_rank": pairwise_rank_agreement,
    }
    if isinstance(loader_test.dataset.data, torch.Tensor) and isinstance(loader_test.dataset.targets, torch.Tensor):
        test_inputs = loader_test.dataset.data[:500]
        test_labels = loader_test.dataset.targets[:500]
    else:
        test_inputs = torch.tensor(loader_test.dataset.data)[:500]
        test_labels = torch.tensor(loader_test.dataset.targets)[:500]
    feature_scores_a = explainer_a.get_explanation(test_inputs, test_labels).detach()
    feature_scores_b = explainer_b.get_explanation(test_inputs, test_labels).detach()
    disagreement_values = {}
    for name in metrics_dict.keys():
        disagreement_values[name] = float(metrics_dict[name](feature_scores_a, feature_scores_b, disagreement_k))
    return disagreement_values


def disagreement_matrices(model, loader_train, loader_test, k, metric=None):
    metrics_dict = {"feature_agreement": feature_agreement,
                    "rank_agreement": rank_agreement,
                    "sign_agreement": sign_agreement,
                    "signed_rank_agreement": signed_rank_agreement,
                    "rank_correlation": rank_correlation,
                    "pairwise_rank": pairwise_rank_agreement,
                    }
    if metric is not None:
        metrics_dict = {metric: metrics_dict[metric]}
    matrices_output = {}
    for name in metrics_dict.keys():
        matrices_output[name] = compute_disagreement_matrix(model,
                                                            metrics_dict[name],
                                                            loader_train,
                                                            loader_test,
                                                            k)
    return matrices_output


def compute_disagreement_matrix(model, metric, loader_train, loader_test, k):
    train_data_tensor = torch.tensor(loader_train.dataset.data)
    explainer_names = ["input_x_gradient",
                       "integrated_gradients",
                       "lime",
                       "shap",
                       "smooth_grad",
                       "vanilla_gradients"]
    explainers = {name: get_explainer(name, model, train_data_tensor) for name in explainer_names}

    grid_idx = [[i, j] for i in explainer_names for j in explainer_names]
    for g in grid_idx:
        g.sort()
    grid_idx = tuple(tuple(g) for g in grid_idx)
    grid_idx = list(set(tuple(grid_idx)))
    grid_idx.sort(key=lambda y: y[0] + y[1])

    disagreement_matrix_dict = {}
    test_inputs = torch.tensor(loader_test.dataset.data)[:500]
    test_labels = torch.tensor(loader_test.dataset.targets)[:500]
    feature_scores = {name: explainers[name].get_explanation(test_inputs, test_labels).detach()
                      for name in explainer_names}
    for i, j in grid_idx:
        disagreement_matrix_dict[i + "_v_" + j] = metric(feature_scores[i], feature_scores[j], k=k).item()
    return disagreement_matrix_dict
