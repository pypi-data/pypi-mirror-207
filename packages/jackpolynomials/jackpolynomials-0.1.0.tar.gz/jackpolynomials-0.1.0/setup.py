# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jackpy']

package_data = \
{'': ['*']}

install_requires = \
['gmpy2>=2.0,<3.0', 'numpy>=1.21.2,<2.0.0', 'sympy>=1.9,<2.0']

extras_require = \
{'docs': ['sphinx>=5.3.0,<6.0.0',
          'sphinx-rtd-theme>=1.1.1,<2.0.0',
          'sphinxcontrib-napoleon>=0.7,<0.8',
          'sphinxcontrib-restbuilder>=0.3,<0.4']}

setup_kwargs = {
    'name': 'jackpolynomials',
    'version': '0.1.0',
    'description': 'Jack polynomials.',
    'long_description': "# jackpolynomials\n\n<!-- badges: start -->\n[![Documentation status](https://readthedocs.org/projects/jackpy/badge/)](http://jackpy.readthedocs.io)\n<!-- badges: end -->\n\nJack polynomials with Python.\n\n```python\n>>> from gmpy2 import mpq\n>>> from sympy.combinatorics.partitions import IntegerPartition\n>>> from jackpy.jack import JackPol\n>>>\n>>> poly = JackPol(3, IntegerPartition([2, 1]), alpha = mpq(3, 2))\n>>> print(poly)\nPoly(7/2*x_0**2*x_1 + 7/2*x_0**2*x_2 + 7/2*x_0*x_1**2 + 6*x_0*x_1*x_2\n + 7/2*x_0*x_2**2 + 7/2*x_1**2*x_2 + 7/2*x_1*x_2**2, x_0, x_1, x_2, domain='QQ')\n```\n",
    'author': 'Stéphane Laurent',
    'author_email': 'laurent_step@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stla/jackpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
