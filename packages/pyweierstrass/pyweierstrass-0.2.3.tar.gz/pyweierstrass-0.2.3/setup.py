# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyweierstrass']

package_data = \
{'': ['*']}

install_requires = \
['mpmath>=1.2.1,<2.0.0']

extras_require = \
{'docs': ['sphinx>=5.3.0,<6.0.0',
          'sphinx-rtd-theme>=1.1.1,<2.0.0',
          'sphinxcontrib-napoleon>=0.7,<0.8',
          'sphinxcontrib-restbuilder>=0.3,<0.4']}

setup_kwargs = {
    'name': 'pyweierstrass',
    'version': '0.2.3',
    'description': 'Weierstrass elliptic functions',
    'long_description': '# pyweierstrass\n\n[![Documentation Status](https://readthedocs.org/projects/pyweierstrass/badge/?version=latest)](https://pyweierstrass.readthedocs.io/en/latest/?badge=latest)\n\nSome Weierstrass functions: p-function, sigma function, zeta function, and \ninverse p-function.\n\n```\npip install pyweierstrass\n```\n\n',
    'author': 'Stéphane Laurent',
    'author_email': 'laurent_step@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stla/pyweierstrass',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
