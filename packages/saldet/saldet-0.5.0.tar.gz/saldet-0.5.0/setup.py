# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['saldet',
 'saldet.dataset',
 'saldet.experiment',
 'saldet.io',
 'saldet.loss',
 'saldet.lr_scheduler',
 'saldet.model',
 'saldet.model.models',
 'saldet.ops',
 'saldet.optimizer',
 'saldet.pl',
 'saldet.plot',
 'saldet.trainer',
 'saldet.transform',
 'saldet.utils']

package_data = \
{'': ['*']}

install_requires = \
['albumentations>=1.3.0,<2.0.0',
 'lightning-bolts>=0.5.0,<0.6.0',
 'matplotlib>=3.7.1,<4.0.0',
 'pytorch-lightning>=2.0.0,<3.0.0',
 'pyyaml>=6.0,<7.0',
 'timm>=0.6.13,<0.7.0',
 'torch>=2.0.1,<3.0.0',
 'torchvision>=0.15.2,<0.16.0',
 'tqdm>=4.65.0,<5.0.0']

setup_kwargs = {
    'name': 'saldet',
    'version': '0.5.0',
    'description': 'Saliency Detection library (models, loss, utils) with PyTorch',
    'long_description': '<p align="center">\n    <img width="100%" src=".static/example_1.png" alt>\n</p>\n\n# saldet\n> **Sal**iency **Det**ection (*saldet*) is a collection of models and tools to perform Saliency Detection with PyTorch.\n\n\n\n[![PyPI Version][pypi-image]][pypi-url]\n[![Build Status][build-image]][build-url]\n[![Code Coverage][coverage-image]][coverage-url]\n\n...\n\n<!-- Badges: -->\n\n[pypi-image]: https://img.shields.io/pypi/v/saldet\n[pypi-url]: https://pypi.org/project/saldet/\n[build-image]: https://github.com/riccardomusmeci/saldet/actions/workflows/build.yaml/badge.svg\n[build-url]: https://github.com/riccardomusmeci/saldet/actions/workflows/build.yaml\n[coverage-image]: https://codecov.io/gh/riccardomusmeci/saldet/branch/main/graph/badge.svg\n[coverage-url]: https://codecov.io/gh/riccardomusmeci/saldet/\n\n## **Models**\nList of saliency detection models supported by saldet:\n\n* U2Net - https://arxiv.org/abs/2005.09007v3\n* PGNet - https://arxiv.org/abs/2204.05041 (follow training instructions from [PGNet\'s repo](https://github.com/iCVTEAM/PGNet))\n\n\n## **Train**\n### **Easy Mode**\nThe library comes with easy access to train models thanks to the amazing PyTorch Lightning support. \n\n```python\nfrom saldet.experiment import train\n\ntrain(\n    data_dir=...,\n    config_path="config/u2net_lite.yaml", # check the config folder with some configurations\n    output_dir=...,\n    resume_from=...,\n    seed=42\n)\n```\n\nOnce the training is over, configuration file and checkpoints will be saved into the output dir.\n\n**[WARNING]** The dataset must be structured as follows:\n```\ndataset\n    ├── train                    \n    |       ├── images          \n    |       │   ├── img_1.jpg\n    |       │   └── img_2.jpg                \n    |       └── masks\n    |           ├── img_1.png\n    |           └── img_2.png   \n    └── val\n           ├── images          \n           │   ├── img_10.jpg\n           │   └── img_11.jpg                \n           └── masks\n               ├── img_10.png\n               └── img_11.png   \n```\n\n### **PyTorch Lighting Mode**\nThe library provides utils for model and data PyTorch Lightning Modules.\n```python\nimport pytorch_lightning as pl\nfrom saldet import create_model\nfrom saldet.pl import SaliencyPLDataModule, SaliencyPLModel\nfrom saldet.transform import SaliencyTransform\n\n# datamodule\ndatamodule = SaliencyPLDataModule(\n    root_dir=data_dir,\n    train_transform=SaliencyTransform(train=True, **config["transform"]),\n    val_transform=SaliencyTransform(train=False, **config["transform"]),\n    **config["datamodule"],\n)\n\nmodel = create_model(...)\ncriterion = ...\noptimizer = ...\nlr_scheduler = ...\n\npl_model = SaliencyPLModel(\n    model=model, criterion=criterion, optimizer=optimizer, lr_scheduler=lr_scheduler\n)\n\ntrainer = pl.Trainer(...)\n\n# fit\nprint(f"Launching training...")\ntrainer.fit(model=pl_model, datamodule=datamodule)\n```\n\n### **PyTorch Mode**\nAlternatively you can define your custom training process and use the ```create_model()``` util to use the model you like.\n\n\n## **Inference**\nThe library comes with easy access to inference saliency maps from a folder with images.\n```python\nfrom saldet.experiment import inference\n\ninference(\n    images_dir=...,\n    ckpt=..., # path to ckpt/pth model file\n    config_path=..., # path to configuration file from saldet train\n    output_dir=..., # where to save saliency maps\n)\n```\n',
    'author': 'Riccardo Musmeci',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/riccardomusmeci/saldet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
