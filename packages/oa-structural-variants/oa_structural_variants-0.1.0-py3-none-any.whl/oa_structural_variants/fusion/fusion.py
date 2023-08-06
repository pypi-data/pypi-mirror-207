from __future__ import annotations

from dataclasses import InitVar, dataclass, field
from pathlib import Path
from typing import Dict, List, Literal

from dna_utils import DNAUtils

from oa_structural_variants import StructuralVariant

from .partner import Partners


@dataclass
class Fusion(StructuralVariant):
    partners: Partners
    reading_frame: Literal["in-frame", "out-of-frame", "stop-codon", "."] = "."
    confidence: Literal["low", "medium", "high", "unknown"] = "unknown"
    filters: int | None = None
    discordant_mates: int | None = None
    tags: List[str] | None = None
    retained_protein_domains: List[str] | None = None
    read_identifiers: str | None = None
    seq: str | None = None
    name_separator: Literal["::", "--"] = "::"
    fasta_ref: InitVar[Path] = None
    metrics: Dict = field(default_factory=dict)

    def __post_init__(self, fasta_ref):
        if fasta_ref:
            self.set_sequence(fasta_ref)

    @property
    def name(self):
        return self.partners.left.name + self.name_separator + self.partners.right.name

    def set_sequence(self, fasta_ref: Path, extend=25):
        self.seq = self.get_sequence(fasta_ref, extend)

    def get_sequence(self, fasta_ref: Path, extend):
        if self.partners.left.fusion_strand == "+":
            bp = str(
                DNAUtils.get_reference_sequence(
                    fasta_ref,
                    self.partners.left.chr,
                    self.partners.left.position - extend,
                    self.partners.left.position,
                )
            )
        else:
            bp = str(
                DNAUtils.reverse_complement(
                    DNAUtils.get_reference_sequence(
                        fasta_ref,
                        self.partners.left.chr,
                        self.partners.left.position,
                        self.partners.left.position + extend,
                    )
                )
            )
        if self.partners.right.fusion_strand == "+":
            bp += str(
                DNAUtils.get_reference_sequence(
                    fasta_ref,
                    self.partners.right.chr,
                    self.partners.right.position,
                    self.partners.right.position + extend,
                )
            )
        else:
            bp += str(
                DNAUtils.reverse_complement(
                    DNAUtils.get_reference_sequence(
                        fasta_ref,
                        self.partners.right.chr,
                        self.partners.right.position - extend,
                        self.partners.right.position,
                    )
                )
            )
        return bp

    @property
    def peptide_sequence(self):
        return DNAUtils.translate(self.seq)

    def format_for_harriba_draw(self):
        if self.seq is None:
            raise Exception("No Seq were set for this fusion." " Please set the seq by using set_sequence method")
        line = [
            self.partners.left.name,
            self.partners.right.name,
            self.partners.left.strand,
            self.partners.right.strand,
            f"{self.partners.left.chr.replace('chr', '')}:{self.partners.left.position}",
            f"{self.partners.right.chr.replace('chr', '')}:{self.partners.right.position}",
            self.partners.left.site,
            self.partners.right.site,
            "fusion",
            self.partners.left.split_reads or 0,
            self.partners.right.split_reads or 0,
            self.discordant_mates or 0,
            self.partners.left.coverage or 0,
            self.partners.right.coverage or 0,
            self.confidence,
            self.reading_frame,
            self.tags or ".",
            self.retained_protein_domains or ".",
            self.partners.left.closest_genomic_breakpoint or ".",
            self.partners.right.closest_genomic_breakpoint or ".",
            self.partners.left.gene_id or ".",
            self.partners.right.gene_id or ".",
            self.partners.left.transcript_id or ".",
            self.partners.right.transcript_id or ".",
            self.partners.left.direction,
            self.partners.right.direction,
            self.filters or ".",
            self.seq,
            self.peptide_sequence,
            self.read_identifiers or ".",
        ]
        return "\t".join(map(str, line))
