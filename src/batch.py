"""Week 6 extension - batch processing, logging, FASTQ and a command-line tool."""
import logging
import sys
from collections.abc import Iterator

LOG = logging.getLogger("batch")


class FastqFormatError(ValueError):
    """Raised when a FASTQ file is malformed."""


def process_directory(in_dir, out_csv, log_path=None) -> dict[str, int]:
    """Read every *.fasta file in in_dir; one bad file never stops the batch.

    Writes one row per file (file, records, status, reason) to out_csv and
    returns {'processed': ..., 'rejected': ..., 'records': ...}.
    """
    raise NotImplementedError("TODO: implement process_directory")


def read_fastq(path) -> Iterator[tuple[str, str, str]]:
    """Yield (read_id, sequence, quality) for each 4-line FASTQ record."""
    raise NotImplementedError("TODO: implement read_fastq")


def mean_phred(quality: str, offset: int = 33) -> float:
    """Mean Phred score of a quality string (Phred+33 by default)."""
    if not quality:
        raise ValueError("Wrong value")
    return sum(ord(c)- offset for c in quality)/ len(quality)


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point. Exit code 0 = all good, 1 = some files rejected, 2 = bad input."""
    raise NotImplementedError("TODO: implement main")


if __name__ == "__main__":
    sys.exit(main())
