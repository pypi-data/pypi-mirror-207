# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tum_esm_utils']

package_data = \
{'': ['*'],
 'tum_esm_utils': ['ifg_parser/.gitignore',
                   'ifg_parser/.gitignore',
                   'ifg_parser/.gitignore',
                   'ifg_parser/.gitignore',
                   'ifg_parser/.gitignore',
                   'ifg_parser/.gitignore',
                   'ifg_parser/.gitignore',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_OPUSparms.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/glob_prepro4.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.F90',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/ifg_parser.template.inp',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec.dat',
                   'ifg_parser/refspec2.dat',
                   'ifg_parser/refspec2.dat',
                   'ifg_parser/refspec2.dat',
                   'ifg_parser/refspec2.dat',
                   'ifg_parser/refspec2.dat',
                   'ifg_parser/refspec2.dat',
                   'ifg_parser/refspec2.dat']}

modules = \
['py']
install_requires = \
['filelock>=3.10.0,<4.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'polars>=0.17.11,<0.18.0',
 'psutil>=5.9.4,<6.0.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'tum-esm-utils',
    'version': '1.5.2',
    'description': 'Python utilities by the Professorship of Environmental Sensing and Modeling at the Technical University of Munich',
    'long_description': '# 🔬 &nbsp;TUM ESM Python Utilities\n\nThis library is a collection of small functions used in our research projects. Here, we can test and document the functions properly instead of every project dealing with this overhead which allows us to reduce the size of the utility directories of individual projects.\n\nFeel free to use it in any other project ✨\n\n[![PyPI](https://img.shields.io/pypi/v/tum-esm-utils?color=f43f5e)](https://pypi.org/project/tum-esm-utils)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tum-esm-utils?color=f43f5e)](https://pypi.org/project/tum-esm-utils/)\n[![GitHub](https://img.shields.io/github/license/tum-esm/utils?color=f59e0b)](https://github.com/tum-esm/utils/blob/main/LICENSE)\n<br/>\n[![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/tum-esm/utils/test.yaml?branch=main&label=CI%20tests)](https://github.com/tum-esm/utils/actions/workflows/test.yaml)\n[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/tum-esm/utils?label=codeclimate%20maintainability%20rating)](https://codeclimate.com/github/tum-esm/utils)\n\n<br/>\n\n## For Users\n\nInstall the Python library with:\n\n```bash\npoetry add tum_esm_utils\n# or\npip install tum_esm_utils\n```\n\nUse the API reference at https://tum-esm.github.io/utils.\n\n<br/>\n\n## For Developers\n\nPublish the Package to PyPI:\n\n```bash\npoetry build\npoetry publish\n```\n\nServe documentation page:\n\n```bash\ndocsify serve ./docs\n```\n',
    'author': 'Moritz Makowski',
    'author_email': 'moritz.makowski@tum.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tum-esm/utils',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
