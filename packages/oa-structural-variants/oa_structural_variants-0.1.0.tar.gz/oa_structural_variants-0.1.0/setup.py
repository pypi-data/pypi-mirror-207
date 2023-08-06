# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oa_structural_variants', 'oa_structural_variants.fusion']

package_data = \
{'': ['*']}

install_requires = \
['dacite>=1.8.0,<2.0.0',
 'dnautils>=0.1.0,<0.2.0',
 'gtfparse>=2.0.1,<3.0.0',
 'pandas>=2.0.0,<3.0.0',
 'polars>=0.16.18,<0.17.0']

setup_kwargs = {
    'name': 'oa-structural-variants',
    'version': '0.1.0',
    'description': '',
    'long_description': '# OA_Structural_Variants\n⚠ This only handle fusion at the moment\n\n## Presentation and motivation\nAims of this library is to present an uniq structural variants format to handle \nmultiple tool format.\nTherefore, each output tool should be converted in standard oncodna structural variants format.\n```mermaid\ngraph TD\n    A[Manta] --> AA[FUSION]\n    B[Fusion_inspector] --> BA[FUSION]\n    C[Arriba] --> CA[FUSION]\n    AA --> Consensus\n    BA --> Consensus\n    CA --> Consensus\n    Consensus --> PLOT\n    Consensus --> KDM_TSV\n    Consensus --> Mercury_TSV\n```\n\n## Git repository\nhttp://gitlab.oncoworkers.oncodna.com/bioinfo/libraries/structural_variants\n\n## Installation\n\n`pip install oa_structural_variants`\n`pip install http://gitlab.oncoworkers.oncodna.com/bioinfo/libraries/structural_variants.git`\n\n## Usage\n\n```python\nfrom oa_structural_variants.fusion import Fusion, Partner, Partners\n## Create fusion object\nfusion = Fusion(\n    partners=Partners(\n        left=Partner(\n            direction="upstream",\n            chr="chr1",\n            position=10,\n        ),\n        right=Partner(\n            direction="downstream",\n            chr="chr1",\n            position=10,\n        )\n    )\n)\n\n## Export fusion object\nfrom oa_structural_variants.utils import save_sv_to_json\n\nsave_sv_to_json(json_path="path_to_output", svs=[fusion])\n\n## Import fusion object\nfrom oa_structural_variants.utils import load_sv_from_json\n\nfusions = load_sv_from_json(json_path="path_to_input")\n```',
    'author': 'Benoitdw',
    'author_email': 'bw@oncodna.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
