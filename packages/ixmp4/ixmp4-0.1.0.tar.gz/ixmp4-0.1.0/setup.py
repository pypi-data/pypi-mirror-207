# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ixmp4',
 'ixmp4.cli',
 'ixmp4.conf',
 'ixmp4.core',
 'ixmp4.core.iamc',
 'ixmp4.data',
 'ixmp4.data.abstract',
 'ixmp4.data.abstract.iamc',
 'ixmp4.data.api',
 'ixmp4.data.api.iamc',
 'ixmp4.data.auth',
 'ixmp4.data.backend',
 'ixmp4.data.db',
 'ixmp4.data.db.iamc',
 'ixmp4.data.db.iamc.datapoint',
 'ixmp4.data.db.iamc.variable',
 'ixmp4.data.db.model',
 'ixmp4.data.db.region',
 'ixmp4.data.db.run',
 'ixmp4.data.db.scenario',
 'ixmp4.data.db.unit',
 'ixmp4.db',
 'ixmp4.db.migrations',
 'ixmp4.db.migrations.versions',
 'ixmp4.db.utils',
 'ixmp4.server',
 'ixmp4.server.rest',
 'ixmp4.server.rest.iamc']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['PyJWT>=2.4.0,<3.0.0',
 'SQLAlchemy-Utils>=0.40.0,<0.41.0',
 'SQLAlchemy[mypy]>=2.0.5,<3.0.0',
 'alembic>=1.10.2,<2.0.0',
 'dask>=2023.4.0,<2024.0.0',
 'fastapi>=0.94.0,<0.95.0',
 'httpx[http2]>=0.23.3,<0.24.0',
 'openpyxl>=3.0.9,<4.0.0',
 'oracledb>=1.2.2,<2.0.0',
 'pandas>=2.0.0,<3.0.0',
 'pandera>=0.13.4,<0.14.0',
 'psycopg2>=2.9.3,<3.0.0',
 'pydantic>=1.10.5,<2.0.0',
 'python-dotenv>=0.19.0,<0.20.0',
 'requests>=2.27.1,<3.0.0',
 'rtoml>=0.8.0,<0.9.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['ixmp4 = ixmp4.__main__:app']}

setup_kwargs = {
    'name': 'ixmp4',
    'version': '0.1.0',
    'description': 'a data warehouse for scenario analysis',
    'long_description': '# The ixmp4 package for scenario data management\n\nCopyright (c) 2023 IIASA - Energy, Climate, and Environment Program (ECE)\n\n[![license: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/iiasa/ixmp4/blob/main/LICENSE)\n[![python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)](https://github.com/iiasa/ixmp4)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## Overview\n\nThe **ixmp4** package is a data warehouse for high-powered scenario analysis\nin the domain of integrated assessment of climate change and energy systems modeling.\n\n## License\n\nThe **ixmp4** package is released under the [MIT license](https://github.com/iiasa/ixmp4/blob/main/LICENSE).\n\n## Requirements\n\nThis project requires Python 3.10 and poetry (>= 1.2).\n\n## Setup\n\n```bash\n# Install Poetry, minimum version >=1.2 required\ncurl -sSL https://install.python-poetry.org | python -\n\n# You may have to reinitialize your shell at this point.\nsource ~/.bashrc\n\n# Activate in-project virtualenvs\npoetry config virtualenvs.in-project true\n\n# Install dependencies\n# (using "--with dev,docs,server" if dev and docs dependencies should be installed as well)\npoetry install --with dev,docs,server\n\n# Activate virtual environment\npoetry shell\n\n# Copy the template environment configuration\ncp template.env .env\n\n# Add a test platform\nixmp4 platforms add test\n\n# Start the asgi server\nixmp4 server start\n```\n\n## CLI\n\n```bash\nixmp4 --help\n```\n\n## Docs\n\nCheck [doc/README.md](doc/README.md) on how to build and serve dev documentation locally.\n\n## Docker Image\n\nCheck [docker/README.md](docker/README.md) on how to build and publish docker images.\n\n## Developing\n\nSee [DEVELOPING.md](DEVELOPING.md) for guidance. When contributing to this project via\na Pull Request, add your name to the "authors" section in the `pyproject.toml` file.\n\n## Funding ackownledgement\n\n<img src="./doc/source/_static/ECEMF-logo.png" width="264" height="100"\nalt="ECEMF logo" />\n<img src="./doc/source/_static/openENTRANCE-logo.png" width="187" height="120"\nalt="openENTRANCE logo" />\n<img src="./doc/source/_static/ariadne-bmbf-logo.png" width="353" height="100"\nalt="Kopernikus project ARIADNE logo" />\n\nThe development of the **ixmp4** package was funded from the EU Horizon 2020 projects\n[openENTRANCE](https://openentrance.eu) and [ECEMF](https://ecemf.eu)\nas well as the BMBF Kopernikus project [ARIADNE](https://ariadneprojekt.de)\n(FKZ 03SFK5A by the German Federal Ministry of Education and Research).\n\n<img src="./doc/source/_static/EU-logo-300x201.jpg" width="80" height="54" align="left"\nalt="EU logo" /> This project has received funding from the European Union’s Horizon\n2020 research and innovation programme under grant agreement No. 835896 and 101022622.\n',
    'author': 'Max Wolschlager',
    'author_email': 'wolschlager@iiasa.ac.at',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://software.ece.iiasa.ac.at',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
