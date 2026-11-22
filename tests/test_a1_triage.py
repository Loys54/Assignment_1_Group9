import pytest
from a1_triage import (
    CSV_COLUMNS,
    classify_variant,
    decision_counts,
    rank_variants,
    results_to_csv,
    triage, build_report,
    triage,impact_counts, gene_summary,
)

group_params = {
    "min_depth" : 12,
    "min_quality" : 80,
    "priority_genes" : ["BRCA1", "MLH1", "TP53", "KRAS", "APC"],
    "top_k":6,
}

depth_below = 11
depth_at =12
depth_above =13

quality_below =79
quality_at =80
quality_above = 81

default_depth =30
default_quality = 90
default_pos =1000
second_pos = 2000

zero_k = 0
large_k = 10
negative_k= -1

count_two= 2
count_three = 3
expected_mean_depth = 17.0

def make_row(
    variant: str = "v1",
    gene: str = "BRCA1",
    chrom: str = "17",
    pos: int | str = default_pos,
    depth: int | str = default_depth,
    quality: int | str = default_quality,
    impact: str = "high",    
) -> dict:
    return {
        "variant": variant,
        "gene": gene,
        "chrom": chrom,
        "pos": str(pos),
        "depth": str(depth),
        "quality": str(quality),
        "impact": impact,
    }

def test_boundary_depth_at_group_treshold():
    d_below, r_below = classify_variant(make_row(depth=depth_below), group_params)
    assert d_below == "exclude"
    assert "depth" in r_below.lower()
    assert str(depth_below) in r_below
    assert str(group_params["min_depth"]) in r_below

    d_at, _ = classify_variant(make_row(depth=depth_at), group_params)
    assert d_at == "prioritize"

    d_above, _ = classify_variant(make_row(depth=depth_above), group_params)
    assert d_above == "prioritize"

def test_boundary_quality_at_group_treshold():
    d_below, r_below = classify_variant(make_row(quality=quality_below), group_params)
    assert d_below == "exclude"
    assert "quality" in r_below.lower()
    assert str(quality_below) in r_below
    assert str(group_params["min_quality"]) in r_below

    
    d_at, _ = classify_variant(make_row(quality=quality_at), group_params)
    assert d_at == "prioritize"

    
    d_above, _ = classify_variant(make_row(quality=quality_above), group_params)
    assert d_above == "prioritize"

def test_rule_order_depth_fires_before_quality_and_gene():
    row = make_row(gene="TP53", depth=depth_below, quality=quality_below, impact="high")
    decision, reason = classify_variant(row, group_params)
    assert decision == "exclude"
    assert "depth" in reason.lower()

def test_normal_rules_three_to_stick_mathcing_hand_trace():
    d3, r3 = classify_variant(make_row(variant="v5", gene="TP53", impact="moderate"), group_params)
    assert d3 == "prioritize"
    assert "tp53" in r3.lower() or "moderate" in r3.lower()

    d4, r4 = classify_variant(make_row(variant="v19", gene="KRAS", impact="modifier"), group_params)
    assert d4 == "review"
    assert "kras" in r4.lower() or "modifier" in r4.lower()

    d5, r5 = classify_variant(make_row(variant="v9", gene="CFTR", impact="high"), group_params)
    assert d5 == "review"
    assert "cftr" in r5.lower() or "high" in r5.lower()

    d6, r6 = classify_variant(make_row(variant="v6", gene="CFTR", impact="modifier"), group_params)
    assert d6 == "exclude"
    assert "cftr" in r6.lower() or "modifier" in r6.lower()

def test_awkward_messy_text_and_numeric_inputs():
    messy_row = {
       "variant": "v_messy",
        "gene": "  tp53 \t",
        "chrom": "17",
        "pos": default_pos,
        "depth": depth_at,
        "quality": quality_at,
        "impact": " HIGH\n", 
    }
    decisions, _=classify_variant(messy_row,group_params)
    assert decisions == "prioritize"

def test_triage_preserves_order_and_does_not_mutate_inputs():
    original_rows = [
        make_row(variant="v1", gene="ATM", depth= depth_below,),
        make_row(variant="v2", gene="TP53", impact="high"),
    ]
    rows_snapshot = [dict(r) for r in original_rows]
    params_snapshot = {
        "min_depth": group_params["min_depth"],
        "min_quality": group_params["min_quality"],
        "priority_genes": list(group_params["priority_genes"]),
        "top_k": group_params["top_k"],
    }

    results = triage(original_rows, group_params)
    assert [r["variant"] for r in results] == ["v1", "v2"]
    assert original_rows == rows_snapshot
    assert group_params == params_snapshot

def test_awkward_empty_list_across_functions():
    results = triage([], group_params)
    assert results == []
    assert decision_counts(results) == {"prioritize": 0, "review": 0, "exclude": 0}
    assert impact_counts(results) == {"high": 0, "moderate": 0, "low": 0, "modifier": 0}
    assert gene_summary(results) == {}
    assert rank_variants(results, group_params["top_k"]) == []

def test_awkward_k_zero_and_k_larger_than_data():
    rows = [
        make_row(variant="v1", gene="BRCA1", impact="high"),
        make_row(variant="v2", gene="CFTR", impact="high"),
        make_row(variant="v3", gene="ATM", depth=depth_below),
    ]
    results = triage(rows, group_params)
    assert rank_variants(results, zero_k) == []
    ranked_all = rank_variants(results, large_k)
    assert len(ranked_all) == count_two
    assert [r["variant"] for r in ranked_all] == ["v1", "v2"]

def test_invalid_negative_k_raises_value_error():
    results = triage([make_row()], group_params)
    with pytest.raises(ValueError):
        rank_variants(results, negative_k)
def test_summaries_csv_and_report_output():
    rows = [
        make_row(variant="v1", gene="CFTR", impact="high", quality=95, depth=40, pos=default_pos),
        make_row(variant="v2", gene="APC", impact="high", quality=85, depth=20, pos=second_pos),
        make_row(variant="v3", gene="APC", impact="high", quality=85, depth=20, pos=default_pos),
        make_row(variant="v4", gene="APC", impact="low", quality=85, depth=depth_below, pos=default_pos),
    ]
    results = triage(rows, group_params)

    assert impact_counts(results) == {"high": count_three, "moderate": 0, "low": 0, "modifier": 0}

    summary = gene_summary(results)
    assert list(summary.keys()) == ["APC", "CFTR"]
    assert summary["APC"]["total"] == count_three
    assert summary["APC"]["mean_depth"] == pytest.approx(expected_mean_depth)

    
    ranked = rank_variants(results, count_three)
    assert [r["variant"] for r in ranked] == ["v3", "v2", "v1"]

    csv_text = results_to_csv(results)
    assert csv_text.endswith("\n")
    assert csv_text.splitlines()[0] == ",".join(CSV_COLUMNS)

    report_text = build_report(results, group_params)
    assert "Thresholds: min_depth=12 min_quality=80" in report_text
    assert "Priority genes: BRCA1, MLH1, TP53, KRAS, APC" in report_text
    assert "Variants: 4" in report_text
    assert "Top 6 variants" in report_text
    assert "1. v3 | APC | high | prioritize" in report_text