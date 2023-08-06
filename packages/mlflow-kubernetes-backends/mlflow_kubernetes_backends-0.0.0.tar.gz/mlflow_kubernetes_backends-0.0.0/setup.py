# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlflow_kubernetes_backends']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mlflow-kubernetes-backends',
    'version': '0.0.0',
    'description': '',
    'long_description': '',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
