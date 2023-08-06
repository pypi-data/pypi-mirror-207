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
 'saldet.trainer',
 'saldet.transform',
 'saldet.utils']

package_data = \
{'': ['*']}

install_requires = \
['albumentations>=1.3.0,<2.0.0',
 'lightning-bolts>=0.5.0,<0.6.0',
 'pytorch-lightning>=2.0.0,<3.0.0',
 'pyyaml>=6.0,<7.0',
 'scriv>=1.3.1,<2.0.0',
 'timm>=0.6.13,<0.7.0',
 'torch>=2.0.1,<3.0.0',
 'torchvision>=0.15.2,<0.16.0',
 'tqdm>=4.65.0,<5.0.0',
 'urllib3>=1.26.15,<2.0.0']

setup_kwargs = {
    'name': 'saldet',
    'version': '0.4.0',
    'description': 'Saliency Detection library (models, loss, utils) with PyTorch',
    'long_description': '# saldet\nSaliency Detection library (models, loss, utils) with PyTorch\n',
    'author': 'Riccardo Musmeci',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
