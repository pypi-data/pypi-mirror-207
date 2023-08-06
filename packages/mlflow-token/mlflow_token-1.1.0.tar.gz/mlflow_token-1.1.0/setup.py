# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlflow_token']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['mlflow-token = mlflow_token.mlflow_token:run']}

setup_kwargs = {
    'name': 'mlflow-token',
    'version': '1.1.0',
    'description': 'Command line tool to retreive access token for mlflow instance',
    'long_description': '# mlflow-token\nObtain an access token for an MLFlow instance deployed behind OAuth2-proxy and\nkeycloak. \n\nThis script will use your current setting of `MLFLOW_TRACKING_URI` to look for\nthe keycloak redirect from it\'s OAuth2-proxy. From there it will start an\nOAuth device flow to allow you to obtain a valid access token. You can use this\nto update your `MLFLOW_TRACKING_TOKEN` by executing the command as\n```shell\n% export $(mlflow-token)\n```\nand following the prompt.\n\n## Usage In Jupyter Notebook\nIf you want to authenticate to an MLFlow instance from within a Jupyter notebook\nyou can add the following lines to a cell:\n```python\nimport mlflow_token\nmlflow_token.setup_mlflow_environment("https://mlflow-demo.software-dev.ncsa.illinois.edu/")\n```\nThis will update the notebook\'s `os.environ` so you can immediately use the \nmlflow SDK. The token will eventually expire, so you may need to occasionally \nre-run the cell.\n\nThe cell will print the url for the user to visit and wait for the device\nflow to complete.\n',
    'author': 'Ben Galewsky',
    'author_email': 'bengal1@illinois.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ncsa/mlflow-token',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
