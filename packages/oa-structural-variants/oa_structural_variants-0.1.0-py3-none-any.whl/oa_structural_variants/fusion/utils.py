from pathlib import Path
from typing import List

from .fusion import Fusion

ARRIBA_HEADER = [
    "#gene1",
    "gene2",
    "strand1(gene/fusion)",
    "strand2(gene/fusion)",
    "breakpoint1",
    "breakpoint2",
    "site1",
    "site2",
    "type",
    "split_reads1",
    "split_reads2",
    "discordant_mates",
    "coverage1",
    "coverage2",
    "confidence",
    "reading_frame",
    "tags",
    "retained_protein_domains",
    "closest_genomic_breakpoint1",
    "closest_genomic_breakpoint2",
    "gene_id1",
    "gene_id2",
    "transcript_id1",
    "transcript_id2",
    "direction1",
    "direction2",
    "filters",
    "fusion_transcript",
    "peptide_sequence",
    "read_identifiers",
]


def fusions_to_arriba(fusions: List[Fusion], output_file: Path | str):
    with open(output_file, "w") as _f:
        _f.write("\t".join(ARRIBA_HEADER))
        _f.write("\n")
        for fusion in fusions:
            _f.write(fusion.format_for_harriba_draw())
            _f.write("\n")
