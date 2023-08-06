import logging
from dataclasses import dataclass
from typing import Literal

import polars as pl


@dataclass
class Partner:
    direction: Literal["downstream", "upstream"]
    chr: str
    position: int
    exon_number: int | None = None
    site: str | None = None
    name: str | None = None
    gene_strand: str | None = None
    gene_id: str | None = None
    transcript_id: str | None = None
    split_reads: int | None = None
    coverage: int | None = None
    closest_genomic_breakpoint: str | None = None

    @property
    def fusion_strand(self):
        return {"downstream": "-", "upstream": "+"}.get(self.direction)

    @property
    def strand(self):
        return f"{self.gene_strand}/{self.fusion_strand}"

    def set_annotation(self, gtf: pl.DataFrame):
        transcript = self._get_transcript(gtf)
        if transcript:
            self.transcript_id = transcript["transcript_id"]
            self.gene_strand = transcript["strand"]
            self.name = transcript["gene_name"]
        else:
            self.site = "intergenic"

    def _get_transcript(self, gtf: pl.DataFrame) -> dict:
        """
        get the main transcript at position:
            1: Get all transcripts at position.
                if 0 found, the position is intergenic
                if 1 found, return the transcript
            2: if > 1 transcripts found
                Return the main transcript
        """
        chr_filtered_gtf = self._get_chr_filtered_gtf(gtf)
        transcript_candidates = chr_filtered_gtf.filter(
            (pl.col("feature") == "transcript") & (pl.col("start") <= self.position) & (pl.col("end") >= self.position)
        )
        if transcript_candidates.height == 0:
            logging.warning(f"No transcript found for {self} -> site is intergenic")
            return None
        elif transcript_candidates.height > 1:
            return self._get_main_transcript(gtf=chr_filtered_gtf)
        return transcript_candidates.row(0, named=True)

    def _get_main_transcript(self, gtf: pl.DataFrame) -> dict:
        main = gtf.filter(
            (pl.col("feature") == "transcript") & (pl.col("start") <= self.position) & (pl.col("end") >= self.position)
        )
        if main.height == 1:
            return main.row(0, named=True)
        elif main.height > 1:
            main_transcript = main.filter(pl.col("tag") == "MANE")  # TODO CHANGE
            if main_transcript.height == 1:
                return main_transcript.row(0, named=True)
        filtered_on_transcript = gtf.filter(pl.col("transcript_id").is_in(main.get_column("transcript_id")))
        filtered_gtf = self.get_transcript_with_most_exons(filtered_on_transcript)
        transcript_candidates = filtered_gtf.filter((pl.col("feature") == "transcript"))
        if transcript_candidates.height == 1:
            return transcript_candidates.row(0, named=True)
        filtered_gtf = get_transcript_with_biggest_cds(filtered_on_transcript)
        return filtered_gtf.filter((pl.col("feature") == "transcript")).row(0, named=True)

    def _get_chr_filtered_gtf(self, gtf: pl.DataFrame) -> pl.DataFrame:
        return gtf.filter((pl.col("seqname") == self.chr))

    def get_transcript_with_most_exons(self, gtf: pl.DataFrame) -> pl.DataFrame:
        transcript_candidates = (
            gtf.filter((pl.col("feature") == "exon"))
            .groupby("transcript_id")
            .count()
            .filter(pl.col("count") == pl.col("count").max())
        ).get_column("transcript_id")
        return gtf.filter((pl.col("transcript_id").is_in(transcript_candidates)))


@dataclass
class Partners:
    left: Partner
    right: Partner

    def set_annotation(self, gtf: pl.DataFrame):
        self.left.set_annotation(gtf)
        self.right.set_annotation(gtf)


def get_transcript_with_biggest_cds(filtered_gtf: pl.DataFrame) -> pl.DataFrame:
    transcript_candidates = (
        filtered_gtf.filter((pl.col("feature") == "CDS"))
        .with_columns([(pl.col("end") - pl.col("start")).alias("length")])
        .groupby("transcript_id")
        .agg(pl.col("length").sum())
        .filter(pl.col("length") == pl.col("length").max())
        .get_column("transcript_id")
    )
    return filtered_gtf.filter((pl.col("transcript_id").is_in(transcript_candidates)))
