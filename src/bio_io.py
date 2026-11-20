"""Week 6 - reading FASTA and CSV safely."""
import csv
from collections.abc import Iterator
from pathlib import Path


class FastaFormatError(ValueError):
    """Raised when a FASTA file does not follow the format."""


def _finish(record_id: str, chunks: list[str], path) -> tuple[str, str]:
    sequence = "".join(chunks).upper()
    if not sequence:
        raise FastaFormatError("Has to follow format")
    return record_id,sequence


def read_fasta(patclearh) -> Iterator[tuple[str, str]]:
    """Yield (record_id, sequence) for every record in a FASTA file.

    The id is the first word of the header. Wrapped lines are joined and the
    sequence is upper-cased. Records are produced one at a time, so large
    files do not have to fit in memory.

    Raises:
        FileNotFoundError: if the file does not exist.
        FastaFormatError: for data before the first header, an empty header
            or a record without sequence.
    """
    file_path = Path(patclearh)
    record_id : str | None = None 
    seq_chunks: list[str] = []

    with file_path.open("r",encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if record_id is not None:
                    if not seq_chunks:
                        raise FastaFormatError(f"Record {record_id} has no sequence")
                    yield record_id, "".join(seq_chunks)

            header_text = line[1:].strip()
            if not header_text:
                raise FastaFormatError(f"Empty header in {file_path}")

            record_id = header_text.split()[0]
            seq_chunks = []
        if record_id is None:
            raise FastaFormatError("Sequence data before first header")
        seq_chunks.append(line.upper())
    if record_id is not None:
        if not seq_chunks:
            raise FastaFormatError(f"Record {record_id} no sequence in {file_path}")
        yield record_id, "".join(seq_chunks)
                


def read_csv_records(path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries (all values are strings)."""
    with Path(path).open("r",encoding="utf-8", newline="") as handle:
        return[dict(row) for row in csv.DictReader(handle)]


def write_csv(rows: list[dict], path, fieldnames: list[str]) -> None:
    """Write rows to a CSV file, creating the parent folder if needed."""
    out = Path(path)
    out.parent.mkdir(parents= True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
