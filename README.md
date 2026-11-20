# SECB3203 Lab 6 - Files and exceptions: bio_io.py and batch.py

Student: <Aloysius Probo, X26EC0012>

## Setup
    python -m venv .venv
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## Run
    python -m pytest                              # all tests
    ruff check src                                # style check
    python src/batch.py data/river --out results/cli
    echo $LASTEXITCODE                            # exit code in PowerShell

## What is in this repository
- `src/bio_io.py` : FastaFormatError, read_fasta, read_csv_records, write_csv
- `src/batch.py` : process_directory, read_fastq, mean_phred, main (command-line tool)
- `tests/` : visible tests and my own tests (test_lab06_own.py)
- `data/` : raw synthetic data, read-only (amplicons.fasta, river/, qc_records.csv, reads.fastq)
- `results/` : files the tool writes (not committed)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Exit codes of batch.py
<Write what exit codes 0, 1 and 2 mean, in your own words.>
