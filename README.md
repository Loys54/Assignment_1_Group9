# Variant Triage Service (SECB3203 Assignment 1)

> Replace the text in this template. The README must let a stranger install, run and test the
> project with the exact commands below. All data are synthetic teaching data, not clinical data.

## Group

- Group ID: <GROUP 9>
- Members: <ALOYSIUS Probo Suryo siswanto(X26EC0012)>, <GUO KEXIN(X26EC0009) >, <BAI HAOXIN (X26EC0003)>

## What this project does

<Three or four sentences: what a variant triage service is, what goes in, what comes out.>

## Set up

```
python -m venv .venv
<activate command for your system>
pip install -r requirements.txt
```

## Run

<Write the exact command. The course command is: python src/a1_triage.py data/variants.csv data/params.json results>
<Say which files appear in results/.>

## Test and lint

```
python -m pytest
ruff check src
```

## Our parameters

## Our parameters

Our thresholds, priority genes and top_k are in data/params.json (`min_depth = 12`, `min_quality = 80`, `priority_genes = ["BRCA1", "MLH1", "TP53", "KRAS", "APC"]`, `top_k = 6`)[cite: 1].
They are read at run time and passed to the functions; they are not typed into the rules[cite: 1, 4].

## Design

See [docs/design.md](docs/design.md) for our system design[cite: 4]. It contains our decomposition table, pseudocode for `classify_variant`, a hand-trace table for variants `v1`–`v6`, `v9`, and `v19` at Group G09 thresholds, our test plan, and our work plan[cite: 1, 4].

## Limitations

- Triage decisions rely only on sequencing `depth`, `quality`, predicted `impact`, and a fixed list of priority genes, without clinical databases, population allele frequencies, or real clinical advice[cite: 4].
- All datasets and thresholds are synthetic teaching data and are not intended for clinical or diagnostic use[cite: 4].
- The implementation uses standard Python structures up to Week 5 scope without classes, NumPy, or pandas, and expects valid numeric values for `depth`, `quality`, and `pos`[cite: 4].

## Who did what

| Member | Main contributions | Commits |
|---|---|---|
| BAI HAOXIN (X26EC0003) | `docs/design.md` (decomposition, pseudocode, hand trace) and `classify_variant`, `triage` in `src/a1_triage.py` | <number> |
| GUO KEXIN (X26EC0009) | `decision_counts`, `impact_counts`, `gene_summary`, and `rank_variants` in `src/a1_triage.py` | <number> |
| Aloysius Probo Suryo Siswanto (X26EC0012) | `results_to_csv`, `build_report`, tests, `README.md`, `GROUP_CONTRACT.md`, `AI_USE_LOG.md`, and `ruff` checks | <number> |

## AI use

See `AI_USE_LOG.md`; our group used generative AI at Level 1 (as a tutor/reference) and verified all code with `pytest` and `ruff`[cite: 4].