"""
Bias-Corrected Health Evidence Engine — Entry Point
=====================================================

Scores all interventions across bias-corrected composite dimensions and
outputs a ranked results JSON file.

Usage:
    python engine/run.py --out_dir results/run_0
    python engine/run.py --out_dir results/run_0 --time_horizon long
    python engine/run.py --out_dir results/run_0 --time_horizon short

Arguments:
    --out_dir       Output directory for results JSON (created if absent)
    --time_horizon  short (1-2yr) | medium (5-10yr, default) | long (20yr+/generational)
    --seed          Random seed for reproducibility (default: 42)
"""

import argparse
import json
import os

import numpy as np

from engine.interventions import INTERVENTIONS
from engine.scoring import score_all, compare_categories, test_hypotheses

parser = argparse.ArgumentParser(description="Bias-corrected health evidence engine")
parser.add_argument("--out_dir", type=str, default="run_0",
                    help="Output directory for results")
parser.add_argument("--time_horizon", type=str, default="medium",
                    choices=["short", "medium", "long"],
                    help="short=1-2yr | medium=5-10yr | long=20yr+/generational")
parser.add_argument("--seed", type=int, default=42)
args = parser.parse_args()

np.random.seed(args.seed)
os.makedirs(args.out_dir, exist_ok=True)

# --- Score all interventions ---
scores = score_all(INTERVENTIONS, time_horizon=args.time_horizon)
category_summary = compare_categories(scores)
hypotheses = test_hypotheses(scores)

# --- Time horizon reversal analysis ---
# Identify interventions where long-term benefit is substantially lower than short-term.
# Pattern: appears effective at 2yr, reveals harm or diminishing returns at 20yr.
reversals = []
for name, iv in INTERVENTIONS.items():
    short = iv.get("time_horizon_short", 0)
    long_ = iv.get("time_horizon_long", 0)
    if short > 0 and long_ < short * 0.7:
        reversals.append({
            "name": name,
            "category": iv["category"],
            "short_term": short,
            "long_term": long_,
            "reversal_magnitude": round((short - long_) / short, 2),
        })

# --- Bias suppression ranking ---
# Interventions with highest bias multiplier (most suppressed in published literature)
suppressed = sorted(
    [s for s in scores if s["bias_multiplier"] > 1.0],
    key=lambda x: x["bias_multiplier"],
    reverse=True
)

# Interventions with highest inflation ratio (most inflated in published literature)
inflated = sorted(
    [s for s in scores if s["bias_inflation_ratio"] > 1.0],
    key=lambda x: x["bias_inflation_ratio"],
    reverse=True
)

# --- Build final output ---
final_info = {
    "run_config": {
        "time_horizon": args.time_horizon,
        "seed": args.seed,
        "n_interventions": len(scores),
    },
    "ranked_interventions": scores,
    "category_summary": category_summary,
    "hypothesis_results": hypotheses,
    "time_horizon_reversals": reversals,
    "most_suppressed_interventions": suppressed[:10],
    "most_inflated_interventions": inflated[:10],
    "means": {
        "lifestyle_adj": round(
            float(np.mean([s["adjusted_composite"] for s in scores
                           if s["category"] == "lifestyle"])), 4
        ) if any(s["category"] == "lifestyle" for s in scores) else 0,
        "pharma_adj": round(
            float(np.mean([s["adjusted_composite"] for s in scores
                           if s["category"] == "pharmaceutical"])), 4
        ) if any(s["category"] == "pharmaceutical" for s in scores) else 0,
        "oral_systemic_adj": round(
            float(np.mean([s["adjusted_composite"] for s in scores
                           if s["category"] == "oral_systemic"])), 4
        ) if any(s["category"] == "oral_systemic" for s in scores) else 0,
        "natural_adj": round(
            float(np.mean([s["adjusted_composite"] for s in scores
                           if s["category"] == "natural"])), 4
        ) if any(s["category"] == "natural" for s in scores) else 0,
    },
}

out_path = os.path.join(args.out_dir, "final_info.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(final_info, f, indent=2, default=str)

print(f"Results written to {out_path}")
print(f"\nTop 10 interventions (adjusted composite, {args.time_horizon}-term):")
for i, s in enumerate(scores[:10], 1):
    print(f"  {i:2d}. {s['name']:<40s} [{s['category']:<15s}] "
          f"adj={s['adjusted_composite']:.4f}  NNT={s['nnt_mortality_10yr']}")

print(f"\nCategory averages (adjusted composite):")
for cat, stats in sorted(category_summary.items(),
                          key=lambda x: x[1]["avg_adjusted_composite"], reverse=True):
    print(f"  {cat:<20s}  avg={stats['avg_adjusted_composite']:.4f}  "
          f"avg_NNT={stats['avg_nnt_mortality_10yr']}")

print(f"\nHypothesis results:")
for h, result in hypotheses.items():
    status = "CONFIRMED" if result["result"] else "NOT CONFIRMED"
    print(f"  {h}: {status}")
