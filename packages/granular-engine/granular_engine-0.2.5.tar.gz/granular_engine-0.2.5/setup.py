# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['engine', 'engine.cli', 'engine.connections', 'engine.libs']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'inquirerpy>=0.3.4,<0.4.0',
 'keyring>=23.11.0,<24.0.0',
 'keyrings-alt>=4.2.0,<5.0.0',
 'passlib>=1.7.4,<2.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'yacs>=0.1.8,<0.2.0']

entry_points = \
{'console_scripts': ['engine = engine.cli:cli']}

setup_kwargs = {
    'name': 'granular-engine',
    'version': '0.2.5',
    'description': 'Experiment tracking for GeoSpatial Machine Learning on GeoEngine',
    'long_description': 'Engine\n======\n\nA Utility Library that assists in Geospatial Machine Learning Experiment\nTracking.\n\nInstallation\n------------\n\n.. code:: shell\n\n   pip install granular-engine\n\nUsage\n-----\n\nCLI\n~~~\n\n.. figure:: https://user-images.githubusercontent.com/2713531/210276844-16d3867d-461c-44ba-870b-00d6d6266dbf.gif\n   :alt: engine_cli\n\n   engine_cli\n\nExperiment Tracking\n~~~~~~~~~~~~~~~~~~~\n\n.. code:: python\n\n   from engine import Engine\n\n   engine = Engine("test_config.yaml")\n\n   for epoch in enumerate(epochs):\n      # train \n      # eval\n      engine.log(step=epoch, train_loss=train_loss, val_loss=val_loss)\n\n   engine.done()\n\nLicense\n-------\n\nGPLv3\n\nDocumentation\n-------------\n\nView documentation ``here <https://engine.granular.ai/>``\\ \\_\n',
    'author': 'Sagar Verma',
    'author_email': 'sagar@granular.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/granularai/engine',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
