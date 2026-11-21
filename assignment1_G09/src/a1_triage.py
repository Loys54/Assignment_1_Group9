"""Assignment 1 - clinical variant triage service (synthetic teaching data only).

Reads variant calls, applies ordered triage rules with named thresholds, records a
reason for every decision and produces summaries, a ranked top-k list, a CSV text
and a short text report. Nothing here is clinical advice.
"""
import csv
import json
import sys
from io import StringIO
from pathlib import Path

DECISIONS = ("prioritize", "review", "exclude")
IMPACT_ORDER = ("high", "moderate", "low", "modifier")
PRIORITY_IMPACTS = frozenset({"high", "moderate"})
CSV_COLUMNS = [
    "variant", "gene", "chrom", "pos", "depth", "quality", "impact", "decision", "reason",
]
CLI_ARGUMENTS = 3


def load_variants(path) -> list[dict]:
    """Read variants.csv into a list of dicts. Every value stays text (Week 6 explains how)."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_params(path) -> dict:
    """Read the group parameters (data/params.json) into a dict."""
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def classify_variant(row: dict, params: dict) -> tuple[str, str]:
    """Return (decision, reason) for one variant row.

    Rules run in this order and the first rule that fires decides:
      1. depth < params["min_depth"]                      -> exclude (low depth)
      2. quality < params["min_quality"]                  -> exclude (low quality)
      3. priority gene and impact high or moderate        -> prioritize
      4. priority gene and impact low or modifier         -> review
      5. other gene and impact high or moderate           -> review
      6. other gene and impact low or modifier            -> exclude
    Gene symbols and impact labels are compared after strip() and case folding.
    depth, quality and pos may arrive as text.
    """
    # Named thresholds come from params, never typed into the rules
    min_depth = params["min_depth"]
    min_quality = params["min_quality"]
    priority_genes = {name.strip().casefold() for name in params["priority_genes"]}

    # CSV values arrive as text, so convert numbers with int()
    depth = int(row["depth"])
    quality = int(row["quality"])
    gene = row["gene"].strip()
    impact = row["impact"].strip().casefold()

    # Rules 1 and 2: quality control (exactly at the threshold passes)
    if depth < min_depth:
        return "exclude", f"rule 1 low depth: depth {depth} below min_depth {min_depth}"
    if quality < min_quality:
        return "exclude", f"rule 2 low quality: quality {quality} below min_quality {min_quality}"

    is_priority_gene = gene.casefold() in priority_genes
    is_strong_impact = impact in PRIORITY_IMPACTS

    # Rules 3 to 6: gene and impact
    if is_priority_gene and is_strong_impact:
        return "prioritize", f"rule 3 priority gene {gene} with {impact} impact"
    if is_priority_gene:
        return "review", f"rule 4 priority gene {gene} with {impact} impact"
    if is_strong_impact:
        return "review", f"rule 5 other gene {gene} with {impact} impact"
    return "exclude", f"rule 6 other gene {gene} with {impact} impact"


def triage(rows: list[dict], params: dict) -> list[dict]:
    """Classify every row. Returns NEW dicts (row fields plus decision and reason), same order.

    The input rows and params are never modified.
    """
    results = []
    for row in rows:
        decision, reason = classify_variant(row, params)
        # Build a NEW dict so the input row is never modified
        results.append({**row, "decision": decision, "reason": reason})
    return results


def decision_counts(results: list[dict]) -> dict[str, int]:
    """Count results for each possible decision."""
    counts = {decision: 0 for decision in DECISIONS}

    for result in results:
        counts[result["decision"]] += 1

    return counts


def impact_counts(results: list[dict]) -> dict[str, int]:
    """Count impact values, ignoring excluded variants."""
    counts = {impact: 0 for impact in IMPACT_ORDER}

    for result in results:
        if result["decision"] == "exclude":
            continue

        impact = result["impact"].strip().casefold()
        counts[impact] += 1

    return counts


def gene_summary(results: list[dict]) -> dict[str, dict]:
    """Return counts and mean depth for every gene."""
    statistics: dict[str, dict] = {}

    for result in results:
        gene = result["gene"].strip().upper()

        if gene not in statistics:
            statistics[gene] = {
                "total": 0,
                "prioritize": 0,
                "review": 0,
                "exclude": 0,
                "depth_sum": 0,
            }

        statistics[gene]["total"] += 1
        statistics[gene][result["decision"]] += 1
        statistics[gene]["depth_sum"] += int(result["depth"])

    summary: dict[str, dict] = {}

    for gene in sorted(statistics):
        data = statistics[gene]
        summary[gene] = {
            "total": data["total"],
            "prioritize": data["prioritize"],
            "review": data["review"],
            "exclude": data["exclude"],
            "mean_depth": round(data["depth_sum"] / data["total"], 1),
        }

    return summary


def rank_variants(results: list[dict], k: int) -> list[dict]:
    """Top k variants that were not excluded, best first.

    Sort by: prioritize before review, then impact (high first), then higher quality,
    then higher depth, then smaller pos. Fewer than k are returned if fewer qualify.

    Raises:
        ValueError: if k is negative.
    """
    raise NotImplementedError("TODO: implement rank_variants")


def results_to_csv(results: list[dict]) -> str:
    """Convert results to CSV text with a header and one row per result."""
    output = StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(CSV_COLUMNS)

    for result in results:
        writer.writerow([result[column] for column in CSV_COLUMNS])

    return output.getvalue()


def build_report(results: list[dict], params: dict) -> str:
    """Build the required plain-text triage report."""
    counts = decision_counts(results)
    top_k = params["top_k"]
    ranked = rank_variants(results, top_k)

    lines = [
        "Variant triage report (synthetic teaching data)",
        (
            f"Thresholds: min_depth={params['min_depth']} "
            f"min_quality={params['min_quality']}"
        ),
        f"Priority genes: {', '.join(params['priority_genes'])}",
        f"Variants: {len(results)}",
    ]

    for decision in DECISIONS:
        lines.append(f"{decision}: {counts[decision]}")

    lines.extend(["", f"Top {top_k} variants"])

    for rank, result in enumerate(ranked, start=1):
        lines.append(
            f"{rank}. {result['variant']} | {result['gene']} | "
            f"{result['impact']} | {result['decision']}"
        )

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    """Command line: python src/a1_triage.py VARIANTS_CSV PARAMS_JSON OUT_DIR."""
    args = sys.argv[1:] if argv is None else argv
    if len(args) != CLI_ARGUMENTS:
        print("usage: python src/a1_triage.py data/variants.csv data/params.json results")
        return 2
    variants_path, params_path, out_dir = args
    rows = load_variants(variants_path)
    params = load_params(params_path)
    results = triage(rows, params)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "triage.csv").write_text(results_to_csv(results), encoding="utf-8")
    report = build_report(results, params)
    (out / "report.txt").write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
