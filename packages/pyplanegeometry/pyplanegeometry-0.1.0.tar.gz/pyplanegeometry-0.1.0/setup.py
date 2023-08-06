# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['planegeometry']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0']

extras_require = \
{'docs': ['sphinx>=5.3.0,<6.0.0',
          'sphinx-rtd-theme>=1.1.1,<2.0.0',
          'sphinxcontrib-restbuilder>=0.3,<0.4']}

setup_kwargs = {
    'name': 'pyplanegeometry',
    'version': '0.1.0',
    'description': 'Plane geometry',
    'long_description': '# PyPlaneGeometry\n\n<!-- badges: start -->\n[![Documentation status](https://readthedocs.org/projects/pyplanegeometry/badge/)](http://pyplanegeometry.readthedocs.io)\n<!-- badges: end -->\n\n\nPlane geometry with Python. This library is a Python translation of my R \npackage [PlaneGeometry](https://github.com/stla/PlaneGeometry) but it contains \nless features so far. Do not hesitate to encourage me if you are interested.\n\n```\npip install pyplanegeometry\n```\n\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/triangularApollonianGasket.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/ApollonianIcosahedralGasket.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/NestedSteinerChains.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/SteinerChainWithEllipse.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/HyperbolicTesselation.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalSteinerChain.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalSteinerChain3D.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/ApollonianGasket.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/NestedSteinerChains.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalNestedSteinerChains.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalNestedSteinerChains3D.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalNestedSteinerChains3D_2.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalNestedSteinerChains3D_3.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/ApollonianGasket.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/ModularTessellation.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/Inversions.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/EllipticalBilliard.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/HyperbolicTesselation2.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/SchottkyCircles.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/MalfattiApollonian.gif)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/Circles_simultaneously_tangent.png)\n\n![](https://github.com/stla/PyPlaneGeometry/raw/main/examples/MalfattiGaskets.gif)\n',
    'author': 'Stéphane Laurent',
    'author_email': 'laurent_step@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stla/PyPlaneGeometry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
