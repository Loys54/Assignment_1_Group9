# Design - Variant Triage Service

Group ID: <group 9>      Thresholds from data/params.json: min_depth = <12>, min_quality = <80>, top_k = <6>

## 1. Decomposition

| Question | Our answer |
|---|---|
| Input | One variant row (a dict with variant, gene, chrom, pos, depth, quality, impact; all values are text) and the params dict |
| Output | A tuple (decision, reason). decision is one of prioritize, review, exclude. reason is text without commas |
| Constraints | min_depth = 12 and min_quality = 80 are read from params, never typed into the rules. Boundaries are inclusive: depth 12 and quality 80 pass. Gene and impact are compared after strip() and case folding |
| Rule order and why the order matters | Rules 1 and 2 (quality control) run first, then rules 3 to 6 (gene and impact). The first rule that fires decides. A variant in a priority gene with low depth must still be excluded, so quality control has to come before the gene rules |
| Out of scope | Clinical advice, real patient data, classes, NumPy and pandas |

## 2. Pseudocode or flowchart of classify_variant


```
FUNCTION classify_variant(row, params):
    depth <- int(row.depth)
    quality <- int(row.quality)
    gene <- strip(row.gene)
    impact <- casefold(strip(row.impact))
    priority_genes <- set of casefolded params.priority_genes

    IF depth < params.min_depth THEN
        RETURN exclude, "rule 1 low depth ..."
    IF quality < params.min_quality THEN
        RETURN exclude, "rule 2 low quality ..."
    IF gene IN priority_genes AND impact IN (high, moderate) THEN
        RETURN prioritize, "rule 3 ..."
    IF gene IN priority_genes THEN                 # impact is low or modifier
        RETURN review, "rule 4 ..."
    IF impact IN (high, moderate) THEN             # other gene
        RETURN review, "rule 5 ..."
    RETURN exclude, "rule 6 ..."                   # other gene, low or modifier
```


## 3. Hand trace

Thresholds: min_depth = 12, min_quality = 80. Priority genes: BRCA1, MLH1, TP53, KRAS, APC.

| Variant | Gene | Depth | Quality | Impact | Rule that fires | Decision | Reason |
|---|---|---|---|---|---|---|---|
| v1 | ATM | 9 | 90 | moderate | 1 | exclude | depth 9 below min_depth 12 |
| v2 | MYC | 10 | 90 | high | 1 | exclude | depth 10 below min_depth 12 |
| v3 | PTEN | 11 | 90 | moderate | 1 | exclude | depth 11 below min_depth 12 |
| v4 | RB1 | 30 | 79 | high | 2 | exclude | quality 79 below min_quality 80 |
| v5 | TP53 | 30 | 80 | moderate | 3 | prioritize | quality 80 equals the threshold so it passes; priority gene with moderate impact |
| v6 | CFTR | 30 | 81 | modifier | 6 | exclude | other gene with modifier impact |
| v19 | KRAS | 23 | 91 | modifier | 4 | review | priority gene with modifier impact |
| v9 | CFTR | 32 | 88 | high | 5 | review | other gene with high impact |

## 4. Test plan

- Normal: priority gene with high impact gives prioritize; other gene with low impact gives exclude.
- Boundary depth: 11 gives exclude, 12 passes, 13 passes.
- Boundary quality: 79 gives exclude, 80 passes, 81 passes.
- Rule order: a priority gene with depth 11 is still excluded by rule 1.
- All six rules each have at least one test, including rule 4 and rule 5.
- Messy text: gene " tp53 " and impact " HIGH " are handled; depth and quality given as text or as numbers both work.
- triage: the input rows and params are not changed; the output order equals the input order; empty list gives empty list.
- Later functions: k = 0, k larger than the data, negative k raises ValueError.

## 5. Work plan

| Member | Task | Order |
|---|---|---|
| BAI HAOXIN | T1 design.md and hand trace; T2 classify_variant and triage | 1 |
| GUO KEXIN | T3 decision_counts, impact_counts, gene_summary; T4 rank_variants | 2 |
| LOYS | T5 results_to_csv, build_report and command line run; T6 own tests, README, ruff; T7 group contract and AI log | 3 |

