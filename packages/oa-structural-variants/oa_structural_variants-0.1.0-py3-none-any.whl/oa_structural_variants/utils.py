import dataclasses
import json
from pathlib import Path
from typing import List

import dacite

from oa_structural_variants.fusion import Fusion


def load_sv_from_json(json_path: Path) -> List[Fusion]:
    # TODO add factory
    structural_variants = []
    with open(json_path) as f:
        svs = json.loads(f.read())["fusions"]
    for sv in svs:
        structural_variants.append(dacite.from_dict(Fusion, data=sv, config=dacite.Config(check_types=False)))
    return structural_variants


# Extends it to all SV
def save_sv_to_json(json_path: Path, svs: List[Fusion]):
    with open(json_path, "w") as f:
        f.write(f"{json.dumps({'fusions': [dataclasses.asdict(fusion) for fusion in svs]}, indent=4)}")
