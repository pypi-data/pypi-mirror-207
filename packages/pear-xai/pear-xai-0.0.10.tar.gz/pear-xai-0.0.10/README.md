# :pear: PEAR: Post-hoc Explainer Agreement Regularization

A repo for training neural networks for post hoc explainer agreement. More details about the results can be found in our paper titled [Reckoning with the Disagreement Problem: Explanation Consensus as a Training Objective](https://arxiv.org/pdf/2303.13299.pdf).


## Getting Started

If you are intersted in using the :pear: PEAR package to train your own models, you can install the package through pip.

```$ pip install pear-xai```

You should then be able to run an example in a python interpreter:

```
$ python
>>> import pear
>>> pear.run_example()
```

If you are interested in cloning this repository and reproducing or building on our experiments, you can install the requirements manually as follows. (This code was developed and tested with Python 3.9.5)

After downloading the repository (or cloning it), install the requirements:

```$ pip install -r requirements.txt```

You can then open and run the Jupyter Notebook [tutorials](notebooks) on reproducing our results.
________________________________________________________________________________________________

## Contributing

We believe in open-source community driven software development. Please open issues and pull requests with any questions or improvements you have.


## Citing Our Work

To cite our work, please reference the paper linked above with the following citation.

```
@article{schwarzschild2023reckoning,
  title={Reckoning with the Disagreement Problem: Explanation Consensus as a Training Objective},
  author={Schwarzschild, Avi and Cembalest, Max and Rao, Karthik and Hines, Keegan and Dickerson, John},
  journal={arXiv preprint arXiv:2303.13299},
  year={2023}
}
```