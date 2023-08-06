# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scgpt', 'scgpt.model', 'scgpt.scbank', 'scgpt.tokenizer', 'scgpt.utils']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=2.3.0,<3.0.0',
 'flash-attn==1.0.1',
 'leidenalg>=0.8.10,<0.9.0',
 'llvmlite>=0.38.0,<0.39.0',
 'numba>=0.55.1,<0.56.0',
 'pandas==1.3.5',
 'scanpy>=1.9.1,<2.0.0',
 'scib>=1.0.3,<2.0.0',
 'scikit-misc>=0.1.4,<0.2.0',
 'scvi-tools>=0.16.0,<0.17.0',
 'torch==1.13.0',
 'torchtext==0.14.0',
 'transformers>=4.18.0,<5.0.0',
 'typing-extensions>=4.2.0,<5.0.0',
 'umap-learn>=0.5.3,<0.6.0']

setup_kwargs = {
    'name': 'scgpt',
    'version': '0.1.0',
    'description': 'Large-scale generative pretrain of single cell using transformer.',
    'long_description': 'None',
    'author': 'Haotian',
    'author_email': 'subercui@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
