# Bias-Corrected Health Evidence Engine

**A reproducible computational framework for comparative health intervention efficacy
under structural funding bias correction**

---

**Author:** Eric Chong  
**Year:** 2026  
**Preprint:** medRxiv (DOI pending)  
**Pre-Registration:** [OSF](https://osf.io/2cbzs)  
**License:** MIT  
**Repository:** [github.com/opennnt/bias-corrected-health-engine](https://github.com/opennnt/bias-corrected-health-engine)

---

> *"Absence of evidence is not evidence of absence — when the funding incentive
> to generate that evidence does not exist."*

---

## Overview

The published health evidence base is not a neutral sample of true intervention
effects. It is structured by patent economics, publication incentives, and
administrative boundaries that systematically distort which interventions appear
effective and by how much.

This engine applies 14 quantifiable, directional bias corrections to raw effect
size estimates for 30+ chronic disease prevention interventions — producing
bias-corrected composite scores, adjusted NNTs, and hypothesis test results that
reflect the evidence as it would appear on a level playing field.

**Core finding:** After correction, lifestyle and oral-systemic interventions show
a **5.6–7x composite efficacy advantage** over pharmaceutical comparators at
5–10 year time horizons. The comparison has never previously been made with
structural funding bias removed.

---

## The Problem

Four well-documented, quantifiable biases systematically distort the published
evidence base in a consistent direction — toward pharmaceutical and away from
non-pharmaceutical efficacy:

| Bias | Magnitude | Source |
|---|---|---|
| Industry funding inflation | OR 3.6–4.0x favorable results | Bekelman et al, JAMA 2003 |
| Surrogate endpoint overuse | ~50–60% predictive accuracy for hard endpoints | Fleming & DeMets, Ann Intern Med 1996 |
| Publication bias | 94% published positive vs. 51% actual (antidepressants) | Turner et al, NEJM 2008 |
| No-patent structural underfunding | ~50–70% of approved drugs derive from natural compounds that cannot be patented | Newman & Cragg, J Nat Prod 2020 |

Standard evidence syntheses — including Cochrane reviews, clinical guidelines,
and comparative effectiveness research — do not correct for any of these distortions.
The resulting comparison between pharmaceutical and non-pharmaceutical chronic disease
prevention is measured on a structurally unlevel playing field.

This engine corrects for all four, plus ten additional vectors specific to the
natural-recovery and oral-systemic domains.

---

## The Oral-Systemic Thesis

One of the engine's most consequential findings concerns a research gap that is
structurally produced rather than scientifically justified.

**The body has no dental system.** The classification of oral health as "dental"
rather than "medical" care is an insurance and billing artifact — not a biological
boundary. Periodontal pathogens (*Porphyromonas gingivalis*, *Fusobacterium
nucleatum*) have been physically isolated from:

- Coronary arterial plaques and cardiac thrombus
- Colorectal, breast, and pancreatic tumor tissue  
- Brain tissue in Alzheimer's disease (Dominy et al, *Science Advances* 2019)
- Metaplastic breast lesions in BRCA1-mutant cells (Hopkins 2026)

The AHA 2025 Scientific Statement formally links periodontal disease to
cardiovascular disease. Periodontal treatment reduces CRP by 0.69 mg/L in
RCT meta-analysis — comparable to pharmaceutical anti-inflammatory agents.

**Adjusted NNT for all-cause mortality at 10 years: ~28**  
Statin primary prevention NNT: 150  
SSRI primary prevention NNT: 200  
Aspirin primary prevention NNT: 250

> **Note on the NNT estimate:** The NNT of 28 is a model-derived point estimate
> (plausible range: 15–60) computed from surrogate and composite endpoints, not a
> single trial-observed mortality endpoint. No MACE-endpoint trial for periodontal
> treatment exists. See METHODOLOGY.md Section 4 for full uncertainty discussion.

The research gap is jurisdictional, not biological. This engine quantifies it
as the `jurisdictional_separation` bias vector and corrects for it explicitly.

---

## Key Findings

Scored across 30+ interventions, 6 outcome dimensions, 5–10 year time horizon:

### Category averages (bias-corrected composite score)

| Category | Avg Adjusted Composite | Avg NNT (mortality, 10yr) |
|---|---|---|
| Natural / herbal | 0.317 | 43 |
| Lifestyle | 0.299 | 16 |
| Oral-systemic | 0.255 | 28 |
| Terrain optimization | 0.138 | 40 |
| Traditional medicine | 0.088 | 80 |
| **Pharmaceutical** | **0.042** | **118** |

### Most suppressed interventions (upward correction applied)

| Intervention | Suppression Factor | Mechanism |
|---|---|---|
| Mistletoe (*Viscum album*) | 3.36x | EU-approved oncology adjuvant; absent from US NCCN guidelines |
| Turkey tail PSK | 3.10x | Japan-approved since 1977; absent from US guidelines |
| FMD cancer protocol | 2.74x | BH composite 0.82; no patent funding for Phase III |

### Most inflated interventions (downward correction applied)

| Intervention | Inflation Ratio | Primary Mechanism |
|---|---|---|
| PPIs (long-term) | 4.41x | Industry funding + time horizon reversal (net harm at 20yr) |
| SSRIs | 3.67x | Publication bias 94%→51% + surrogate endpoint + industry funding |
| Statins (primary prevention) | 3.11x | Industry funding + LDL surrogate + T2D risk accumulation |

### Pre-specified hypothesis results

| Hypothesis | Result |
|---|---|
| H1: Lifestyle dominates pharma after correction | **Confirmed** (5.56x advantage) |
| H2: Oral-systemic comparable to pharma | **Confirmed** (NNT 28 vs 118) |
| H3: Natural compounds comparable to pharma | **Confirmed** |
| H4: Top 5 interventions dominated by non-pharma | **Confirmed** (5/5 non-pharma) |
| H5: Blue Zone / healthy-pop validated interventions outperform pharma | **Confirmed** |

---

## Installation

Requires Python 3.8+ and NumPy. No other dependencies.

```bash
git clone https://github.com/opennnt/bias-corrected-health-engine
cd bias-corrected-health-engine
pip install numpy
```

---

## Usage

**Command line:**

```bash
# Medium time horizon (5–10yr, default)
python -m engine.run --out_dir results/run_0

# Long time horizon (20yr+ / generational)
python -m engine.run --out_dir results/long_term --time_horizon long

# Short time horizon (1–2yr)
python -m engine.run --out_dir results/short_term --time_horizon short
```

**Python API:**

```python
from engine import INTERVENTIONS, score_all, compare_categories, test_hypotheses

# Score all interventions
results = score_all(INTERVENTIONS, time_horizon="medium")

# Category summary
cats = compare_categories(results)
print(cats["pharmaceutical"]["avg_adjusted_composite"])  # 0.0422

# Hypothesis testing
h = test_hypotheses(results)
print(h["H1_lifestyle_dominates_pharma"])
# {"result": True, "lifestyle_avg": 0.2993, "pharma_avg": 0.0422, "advantage_ratio": 7.09}

# Score a single intervention
from engine import score_intervention, INTERVENTIONS
result = score_intervention("oral_infection_elimination",
                            INTERVENTIONS["oral_infection_elimination"])
print(result["adjusted_composite"])   # 0.255
print(result["nnt_mortality_10yr"])   # 28
print(result["bias_vectors_applied"]) # list of corrections with magnitudes
```

---

## Repository Structure

```
engine/
  __init__.py        — public API
  bias_vectors.py    — 14 bias vector definitions with evidence sources
  interventions.py   — intervention library (30+ entries, all categories)
  scoring.py         — multiplicative bias correction and composite scoring
  run.py             — CLI entry point → results/run_N/final_info.json

METHODOLOGY.md       — full methodology paper (preprint source)
PREPRINT_ABSTRACT.md — medRxiv abstract and submission guide
LICENSE              — MIT
```

---

## Extending the Engine

### Adding an intervention

Add an entry to `engine/interventions.py`. Minimum required fields:

```python
"intervention_name": {
    "category": "natural",           # lifestyle | oral_systemic | terrain |
                                     # natural | pharmaceutical | traditional
    "outcome_mortality_rrr": 0.15,   # relative risk reduction, 0.0–1.0
    "outcome_cvd_rrr": 0.20,         # negative values = net harm
    "outcome_cancer_rrr": 0.10,
    "outcome_metabolic_rrr": 0.15,
    "outcome_mental_rrr": 0.08,
    "outcome_system_rrr": 0.12,
    "funding_independent_pct": 0.75, # 0.0–1.0
    "hard_endpoints": True,          # True = mortality/MI/stroke; False = surrogate
    "evidence_grade": "B",           # A / B / C / D
    "no_patent_bias": True,
    "jurisdictional_bias": False,
    "typical_nnt_mortality_10yr": 40,
    "disease_reversal_rate": 0.10,
    "healthy_pop_validated": False,
    "adherence_adjusted_rrr": 0.22,
    "time_horizon_short": 0.12,
    "time_horizon_long": 0.20,
    "source": "Citations here",
}
```

### Adding a bias vector

1. Add the vector definition to `engine/bias_vectors.py` with type, direction,
   magnitude, and evidence source
2. Add the correction logic to `compute_bias_multiplier()` in `engine/scoring.py`

### Modifying outcome weights

Weights are defined in `scoring.py::OUTCOME_WEIGHTS` and fully documented.
Mortality (0.30) and CVD (0.20) are weighted highest; whole-system outcome (0.07)
is included as a separate dimension to capture disease reversal, not just management.

---

## Methodology

The full methodology paper is in [`METHODOLOGY.md`](METHODOLOGY.md), covering:

- Theoretical basis for multiplicative vs. additive bias correction
- Evidence basis for each of the 14 bias vector magnitudes
- The oral-systemic jurisdictional separation thesis in detail
- Bradford-Hill mechanistic weight framework
- Exceptional responder / Bayesian mixture cure model application
- Scoring model equations, outcome weights, and composite formula
- Known limitations and proposed validation tests

A preprint is available on medRxiv at: **DOI pending**

---

## Limitations

- Effect sizes are estimated from the published literature and adjusted for documented
  bias patterns. Correction reduces but does not eliminate circularity with the
  distorted source. Independent primary data collection is the long-term solution.
- Correction factor magnitudes are point estimates. Future versions will propagate
  uncertainty to produce confidence intervals on adjusted composites.
- Population-level NNTs obscure heterogeneous treatment effects. Exceptional responder
  analysis is a step toward capturing individual variation; it is not a substitute for
  prospective enrichment studies.
- This engine addresses chronic disease prevention efficacy. It does not evaluate
  acute care, where pharmaceutical intervention is clearly indicated and this bias
  model does not apply.

---

## Citation

If you use this engine in research, please cite:

```
Chong, E. (2026). Multi-Vector Bias Correction for Comparative Health Intervention
Efficacy: A Computational Framework Applied to Pharmaceutical vs. Non-Pharmaceutical
Chronic Disease Prevention. medRxiv. doi:[pending]

@misc{chong2026biascorrected,
  author    = {Chong, Eric},
  title     = {Multi-Vector Bias Correction for Comparative Health Intervention Efficacy},
  year      = {2026},
  publisher = {medRxiv},
  doi       = {pending},
  url       = {https://github.com/opennnt/bias-corrected-health-engine}
}
```

---

## Contributing

Open an issue to:
- Propose a new intervention with supporting sources
- Challenge an existing effect size estimate
- Propose a new bias vector with documented magnitude
- Propose the Vioxx/Rezulin retrovalidation test

All correction factors must be traceable to published evidence.
Pull requests welcome.

---

## License

MIT License. Copyright (c) 2026 Eric Chong / opennnt.  
Use freely. Attribute the work.
