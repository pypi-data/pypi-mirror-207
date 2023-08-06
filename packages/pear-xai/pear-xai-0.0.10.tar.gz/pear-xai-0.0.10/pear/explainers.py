"""
explainers.py
A collection of explainers.
September 2022
"""

from abc import ABC, abstractmethod

import torch
from captum._utils.models import SkLearnLasso
from captum.attr import IntegratedGradients, KernelShap, Saliency, Lime, InputXGradient, NoiseTunnel


class Explainer(ABC):
    def __init__(self, model: torch.nn.Module) -> None:
        """
        Abstract class to implement custom explanation methods for a given.

        :param model: pytorch NN module
        """
        self.model = model

    @abstractmethod
    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        pass


class InputXGradientExplainer(Explainer):
    def __init__(self, model: torch.nn.Module, train_data: torch.Tensor):
        """
        Explainer class for Integrated Gradients

        :param model: torch nn.module
        """
        self.explainer = InputXGradient(model)
        self.train_data = train_data
        super(InputXGradientExplainer, self).__init__(model)

    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        inputs.requires_grad = True
        attributions = self.explainer.attribute(inputs, target=label)
        return attributions


class IntegratedGradientsExplainer(Explainer):
    def __init__(self, model: torch.nn.Module, train_data: torch.Tensor):
        """
        Explainer class for Integrated Gradients

        :param model: torch nn.module
        """
        self.explainer = IntegratedGradients(model, multiply_by_inputs=False)
        self.train_data = train_data
        super(IntegratedGradientsExplainer, self).__init__(model)

    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        inputs.requires_grad = True
        attributions = self.explainer.attribute(inputs,
                                                baselines=self.train_data.mean(dim=0).unsqueeze(0),
                                                target=label,
                                                return_convergence_delta=False,
                                                n_steps=20)
        return attributions


class LimeExplainer(Explainer):
    def __init__(self, model: torch.nn.Module, train_data: torch.Tensor):
        """
        Explainer class for KernelShap

        :param model: torch nn.module
        """
        self.explainer = Lime(model, interpretable_model=SkLearnLasso(alpha=0.0001))
        self.train_data = train_data
        super(LimeExplainer, self).__init__(model)

    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        attributions = self.explainer.attribute(inputs, n_samples=200, target=label)
        return attributions


class KernelShapExplainer(Explainer):
    def __init__(self, model: torch.nn.Module, train_data: torch.Tensor):
        """
        Explainer class for KernelShap

        :param model: torch nn.module
        """
        self.explainer = KernelShap(model)
        self.train_data = train_data
        super(KernelShapExplainer, self).__init__(model)

    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        attributions = self.explainer.attribute(inputs,
                                                n_samples=200,
                                                baselines=self.train_data.mean(dim=0).unsqueeze(0),
                                                target=label)
        return attributions


class SmoothGradExplainer(Explainer):
    def __init__(self, model: torch.nn.Module, train_data: torch.Tensor):
        """
        :param model: torch nn.module
        """
        self.explainer = NoiseTunnel(Saliency(model))
        super(SmoothGradExplainer, self).__init__(model)

    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        inputs.requires_grad = True
        attributions = self.explainer.attribute(inputs, nt_type='smoothgrad', nt_samples=10, target=label, abs=False)
        return attributions


class VanillaGradExplainer(Explainer):
    def __init__(self, model: torch.nn.Module, train_data: torch.Tensor):
        """
        :param model: torch nn.module
        """
        self.explainer = Saliency(model)
        super(VanillaGradExplainer, self).__init__(model)

    def get_explanation(self, inputs: torch.tensor, label: torch.Tensor) -> torch.Tensor:
        """
        Generate explanations for given input/s.

        :param inputs: torch tensor for inferences to be explained - shape (m, n)
        :param label: torch tensor for labels - shape (m, )
        :returns torch.tensor of shape (m, n) with feature scores
        """
        inputs.requires_grad = True
        attributions = self.explainer.attribute(inputs, target=label, abs=False)
        return attributions


def get_explainer(name: str, model: torch.nn.Module, train_data: torch.Tensor) -> Explainer:
    if name == "input_x_gradient":
        return InputXGradientExplainer(model, train_data)
    elif name == "integrated_gradients":
        return IntegratedGradientsExplainer(model, train_data)
    elif name == "lime":
        return LimeExplainer(model, train_data)
    elif name == "shap":
        return KernelShapExplainer(model, train_data)
    elif name == "smooth_grad":
        return SmoothGradExplainer(model, train_data)
    elif name == "vanilla_gradients":
        return VanillaGradExplainer(model, train_data)
    else:
        raise ValueError(f"Explainer {name} not yet implemented.")


def get_a_batch_of_explanations(model, loader_train, loader_test):
    explainer_names = ["input_x_gradient",
                       "integrated_gradients",
                       "lime",
                       "shap",
                       "smooth_grad",
                       "vanilla_gradients"]
    train_data_tensor = torch.tensor(loader_train.dataset.data)
    explainers = {name: get_explainer(name, model, train_data_tensor) for name in explainer_names}
    test_inputs, test_labels = iter(loader_test).next()
    explanations = {name: explainers[name].get_explanation(test_inputs, test_labels).detach()
                    for name in explainer_names}
    return explanations
