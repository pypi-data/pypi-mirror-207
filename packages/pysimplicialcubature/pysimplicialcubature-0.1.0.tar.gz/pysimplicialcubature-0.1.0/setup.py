# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysimplicialcubature']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.5,<2.0.0', 'sympy>=1.11.1,<2.0.0']

extras_require = \
{'docs': ['sphinx>=5.3.0,<6.0.0',
          'sphinx-rtd-theme>=1.1.1,<2.0.0',
          'sphinxcontrib-napoleon>=0.7,<0.8',
          'sphinxcontrib-restbuilder>=0.3,<0.4']}

setup_kwargs = {
    'name': 'pysimplicialcubature',
    'version': '0.1.0',
    'description': 'Integration on simplices.',
    'long_description': '# pysimplicialcubature\n\n<!-- badges: start -->\n[![Documentation status](https://readthedocs.org/projects/pysimplicialcubature/badge/)](http://pysimplicialcubature.readthedocs.io)\n<!-- badges: end -->\n\nThis package is a port of a part of the R package **SimplicialCubature**, \nwritten by John P. Nolan, and which contains R translations of \nsome Matlab and Fortran code written by Alan Genz. In addition it \nprovides a function for the exact computation of the integral of a \npolynomial over a simplex.\n\n___\n\nA simplex is a triangle in dimension 2, a tetrahedron in dimension 3. \nThis package provides two main functions: `integrateOnSimplex`, to integrate \nan arbitrary function on a simplex, and `integratePolynomialOnSimplex`, to \nget the exact value of the integral of a multivariate polynomial on a \nsimplex.\n\nSuppose for example you want to evaluate the following integral:\n\n$$\\int\\_0^1\\int\\_0^x\\int\\_0^y \\exp(x + y + z) \\text{d}z \\text{d}y \\text{d}x.$$\n\n```python\nfrom pysimplicialcubature.simplicialcubature import integrateOnSimplex\nfrom math import exp\n\n# simplex vertices\nv1 = [0.0, 0.0, 0.0] \nv2 = [1.0, 1.0, 1.0] \nv3 = [0.0, 1.0, 1.0] \nv4 = [0.0, 0.0, 1.0]\n# simplex\nS = [v1, v2, v3, v4]\n# function to integrate\nf = lambda x : exp(x[0] + x[1] + x[2])\n# integral of f on S\nI_f = integrateOnSimplex(f, S)\nI_f["integral"]\n```\n\nNow let\'s turn to a polynomial example. You have to define the polynomial with \n`sympy.Poly`.\n\n```python\nfrom pysimplicialcubature.simplicialcubature import integratePolynomialOnSimplex\nfrom sympy import Poly\nfrom sympy.abc import x, y, z\n\n# simplex vertices\nv1 = [1.0, 1.0, 1.0] \nv2 = [2.0, 2.0, 3.0] \nv3 = [3.0, 4.0, 5.0] \nv4 = [3.0, 2.0, 1.0]\n# simplex\nS = [v1, v2, v3, v4]\n# polynomial to integrate\nP = Poly(x**4 + y + 2*x*y**2 - 3*z, x, y, z, domain = "RR")\n# integral of P on S\nintegratePolynomialOnSimplex(P, S)\n```\n\n\n## References\n\n- A. Genz and R. Cools. \n*An adaptive numerical cubature algorithm for simplices.* \nACM Trans. Math. Software 29, 297-308 (2003).\n\n- Jean B. Lasserre.\n*Simple formula for the integration of polynomials on a simplex.* \nBIT Numerical Mathematics 61, 523-533 (2021).',
    'author': 'Stéphane Laurent',
    'author_email': 'laurent_step@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stla/PySimplicialCubature',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
