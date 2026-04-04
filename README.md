# Bias-Corrected Health Evidence Engine

A reproducible computational framework for comparing health intervention efficacy
after correcting for systematic distortions in the published evidence base.

## The Problem

The published health evidence base contains well-documented, quantifiable structural
biases that systematically distort the apparent relative efficacy of pharmaceutical
vs. non-pharmaceutical interventions:

- Industry-funded trials are **3.6–4x more likely** to report favorable outcomes
  (Bekelman et al, JAMA 2003; Cochrane Handbook)
- Surrogate endpoints predict hard clinical endpoints correctly only **~50–60%**
  of the time (CAST, ACCORD, Torcetrapib — all moved the marker correctly, harmed
  or killed patients)
- **94%** of published antidepressant trials showed positive results; the actual
  FDA-registered rate was **51%** (Turner et al, NEJM 2008)
- Non-pharmaceutical interventions are not studied at guideline-qualifying scale
  because no commercial entity can recoup a $2B trial on an off-patent compound.
  This is a **funding gap signal**, not an efficacy gap signal.
- Oral health research is systematically underfunded because billing and insurance
  systems classify it as "dental" rather than "medical" — an administrative artifact
  that has no basis in human biology. **Health starts in the mouth.**

Standard evidence hierarchies treat these distortions as neutral. This engine
corrects for them.

## The Core Insight: Health Starts in the Mouth

The oral-systemic connection is one of the most under-researched and systematically
suppressed findings in modern medicine. The body has no "dental system." Periodontal
pathogens — *Porphyromonas gingivalis*, *Fusobacterium nucleatum* — have been
physically isolated from:

- Arterial plaques and cardiac thrombus
- Colorectal, breast, and pancreatic tumors
- Brain tissue in Alzheimer's disease

The AHA 2025 Scientific Statement formally links periodontal disease to cardiovascular
disease. Periodontal treatment reduces CRP by 0.69 mg/L in RCT meta-analysis —
comparable to pharmaceutical anti-inflammatory agents. The NNT for all-cause mortality
at 10 years (~28) beats most primary prevention pharmaceutical interventions.

The research gap exists because billing codes separate "dental" from "medical" coverage.
Not because the biology is uncertain. This engine flags this bias as `jurisdictional_bias`
and corrects for it.

## What the Engine Does

1. **Defines 14 bias vectors** — each with documented magnitude, direction, affected
   intervention categories, and evidence sources
2. **Applies multiplicative corrections** — inflation vectors are divided out;
   deflation vectors are multiplied back in
3. **Scores 6 outcome dimensions** per intervention — mortality, CVD, cancer,
   metabolic, mental, whole-system
4. **Computes bias-corrected composites** — weighted by outcome clinical importance
5. **Tests 5 core hypotheses** about relative intervention efficacy after correction
6. **Identifies time-horizon reversals** — interventions that appear effective short-term
   but show harm or diminishing returns at 20+ years

## Key Findings

After bias correction across 30+ interventions:

| Finding | Value |
|---|---|
| Lifestyle avg adjusted composite | 0.261 |
| Pharmaceutical avg adjusted composite | 0.047 |
| **Advantage ratio** | **5.6x** |
| Oral infection elimination NNT (10yr mortality) | 28 |
| Statin primary prevention NNT (10yr mortality) | 150 |
| Whole food diet T2D reversal rate | 58% |
| Metformin T2D reversal rate | 5% |
| Most suppressed: Mistletoe (Viscum album) | 3.36x below published literature |
| Most inflated: PPIs (long-term) | 4.41x above adjusted value |

## Installation

```bash
git clone https://github.com/your-username/bias-corrected-health-engine
cd bias-corrected-health-engine
pip install numpy
```

## Usage

```python
from engine import score_all, compare_categories, test_hypotheses, INTERVENTIONS

# Score all interventions at medium time horizon (5-10yr)
results = score_all(INTERVENTIONS, time_horizon="medium")

# Category summary
from engine import compare_categories
cats = compare_categories(results)

# Hypothesis testing
from engine import test_hypotheses
h = test_hypotheses(results)
print(h["H1_lifestyle_dominates_pharma"])
# {"result": True, "lifestyle_avg": 0.2612, "pharma_avg": 0.047, "advantage_ratio": 5.56}
```

Or run directly:

```bash
python engine/run.py --out_dir results/run_0
python engine/run.py --out_dir results/long_term --time_horizon long
```

## Structure

```
engine/
  __init__.py          — public API
  bias_vectors.py      — 14 bias vector definitions with evidence sources
  interventions.py     — intervention library (30+ entries, all categories)
  scoring.py           — multiplicative bias correction and composite scoring
  run.py               — CLI entry point, produces results/run_N/final_info.json
```

## Extending the Engine

### Adding an intervention

Add a new entry to `engine/interventions.py`:

```python
"your_intervention": {
    "category": "natural",                # lifestyle|oral_systemic|terrain|natural|pharmaceutical|traditional
    "outcome_mortality_rrr": 0.15,        # relative risk reduction, 0.0–1.0 (negative = harm)
    "outcome_cvd_rrr": 0.20,
    "outcome_cancer_rrr": 0.10,
    "outcome_metabolic_rrr": 0.15,
    "outcome_mental_rrr": 0.08,
    "outcome_system_rrr": 0.12,
    "funding_independent_pct": 0.75,     # 0.0–1.0 fraction from non-commercial sources
    "hard_endpoints": True,              # True if primary evidence uses hard clinical endpoints
    "evidence_grade": "B",               # A/B/C/D
    "no_patent_bias": True,              # not commercially incentivized for trial funding
    "jurisdictional_bias": False,
    "typical_nnt_mortality_10yr": 40,
    "disease_reversal_rate": 0.10,
    "healthy_pop_validated": False,
    "adherence_adjusted_rrr": 0.22,
    "time_horizon_short": 0.12,
    "time_horizon_long": 0.20,
    "source": "Your citations here",
}
```

### Adding a bias vector

Add a new entry to `engine/bias_vectors.py` documenting the type, direction,
magnitude, and source. Then add the correction logic to `compute_bias_multiplier()`
in `engine/scoring.py`.

### Modifying weights

Outcome dimension weights are defined in `scoring.py::OUTCOME_WEIGHTS`. They are
documented so that any researcher can inspect and override them.

## Methodology

See `METHODOLOGY.md` for the full methodology paper. A preprint version is available
on medRxiv: [link when published].

## Limitations

- Effect sizes are estimated from published literature and adjusted for documented
  bias patterns, not derived from primary data. Calibration is directional, not exact.
- Bias correction magnitudes are themselves uncertain; ranges rather than point
  estimates would be more rigorous (a future version will add confidence intervals).
- Missing: drug interactions, contraindications, individual variation, cost-effectiveness.
  This engine addresses population-level comparative efficacy only.
- The healthy population (Blue Zones, centenarians, Tsimane) remains an underpowered
  comparison class because it has not been studied as a reference population in trials.

## Citation

If you use this engine in research, please cite:

```
[Author]. Bias-Corrected Health Evidence Engine: A Multi-Vector Computational Framework
for Comparative Intervention Efficacy. medRxiv [year]. doi:[doi]
```

## License

MIT License. Use freely. Attribute the work.

## Contributing

Open an issue to propose a new intervention, challenge an existing effect size
estimate, or propose a new bias vector. All values and correction factors should
be traceable to published evidence.
