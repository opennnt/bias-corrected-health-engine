# Pre-Registration: Multi-Vector Bias Correction for Comparative Health Intervention Efficacy

## Authors

Eric Chong, opennnt

## Date

2026-04-05

---

## 1. Study Design

Computational evidence synthesis framework. This study applies a set of pre-specified
bias correction vectors to published effect size estimates for 30+ health interventions
across 6 categories. No primary data collection is involved. The intervention list,
bias vectors, scoring model, outcome weights, and directional hypotheses are fully
specified before any public release of results.

The framework compares pharmaceutical and non-pharmaceutical chronic disease prevention
interventions after applying multiplicative corrections for documented, directional,
quantifiable distortions in the published evidence base. Corrections are derived from
published meta-evidence (Bekelman 2003, Turner 2008, Newman & Cragg 2020, and others).

---

## 2. Disclosure of Prior Data Knowledge

**The bias-corrected health evidence engine has been developed and run prior to this
pre-registration. Results exist in the repository.**

This pre-registration locks the methodology, intervention list, and directional
predictions for the purpose of:

(a) Establishing a timestamped record of the analytical framework  
(b) Enabling falsifiability testing via the proposed retrovalidation method (Section 10)  
(c) Preventing post-hoc claims of cherry-picking  

All intervention definitions, bias vector magnitudes, scoring parameters, and
hypothesis tests are embedded in the source code and can be independently verified
by running the engine. The code repository is the ground truth.

---

## 3. Complete Intervention List

All interventions are extracted from `engine/interventions.py`. Each includes
multi-dimensional effect size estimates across 6 outcome dimensions, funding
independence metadata, and bias correction flags.

| # | Intervention | Category | Hard Endpoints | Evidence Grade |
|---|---|---|---|---|
| 1 | Aerobic exercise | lifestyle | True | A |
| 2 | Sleep optimization | lifestyle | True | B |
| 3 | Whole food diet | lifestyle | True | A |
| 4 | Smoking cessation | lifestyle | True | A |
| 5 | Stress management and purpose | lifestyle | False | B |
| 6 | Social connection | lifestyle | True | B |
| 7 | Resistance training | lifestyle | True | B |
| 8 | Alcohol cessation | lifestyle | True | B |
| 9 | Oral infection elimination | oral_systemic | True | B |
| 10 | Microbiome restoration | terrain | False | B |
| 11 | Toxin reduction | terrain | False | C |
| 12 | Vitamin D optimization | terrain | False | B |
| 13 | Berberine | natural | False | B |
| 14 | Fasting-mimicking diet (FMD) | natural | True | B |
| 15 | Turkey tail PSK | natural | True | B |
| 16 | Mistletoe (Viscum album) | natural | True | B |
| 17 | Curcumin with piperine | natural | False | C |
| 18 | High-dose IV vitamin C | natural | False | C |
| 19 | Omega-3 high-dose EPA | natural | True | B |
| 20 | Melatonin oncology adjuvant | natural | True | B |
| 21 | Statins (primary prevention) | pharmaceutical | False | A |
| 22 | Antihypertensives | pharmaceutical | True | A |
| 23 | SSRI antidepressants | pharmaceutical | False | B |
| 24 | Metformin (T2D) | pharmaceutical | True | A |
| 25 | PPIs (long-term) | pharmaceutical | False | C |
| 26 | TCM acupuncture (chronic pain) | traditional | False | B |

**Category counts:** 8 lifestyle, 1 oral-systemic, 3 terrain, 8 natural, 5 pharmaceutical, 1 traditional.

**Total: 26 interventions** across 6 categories. The engine is designed to be extended
as new interventions with supporting evidence are added.

---

## 4. Pre-Specified Directional Hypotheses

These hypotheses are defined in `engine/scoring.py::test_hypotheses()` and are
tested programmatically against the scored output. Each hypothesis has a precise
computational definition with pass/fail logic.

**H1: Lifestyle dominates pharmaceutical after bias correction**  
After applying all bias correction vectors, lifestyle interventions will show higher
average composite efficacy than pharmaceutical interventions at medium time horizons
(5-10 years). Test: `lifestyle_avg > pharma_avg`.

**H2: Oral-systemic interventions comparable or superior to pharmaceutical**  
Oral infection elimination (periodontal treatment as systemic disease prevention)
will show comparable or superior adjusted composite efficacy to the pharmaceutical
category average. Test: `oral_avg > pharma_avg * 0.8`.

**H3: Natural compound interventions comparable or superior to pharmaceutical**  
Natural/herbal compound interventions, after applying no-patent underfunding,
Bradford-Hill mechanistic, bioavailability, and other deflation corrections, will
show comparable or superior adjusted composite efficacy to pharmaceutical
interventions. Test: `natural_avg > pharma_avg * 0.7`.

**H4: Top 5 interventions dominated by non-pharmaceutical categories**  
When all interventions are ranked by bias-corrected composite score, at least 4
of the top 5 will be from non-pharmaceutical categories (lifestyle, oral-systemic,
terrain, natural, or traditional). Test: `non_pharma_count_in_top5 >= 4`.

**H5: Blue Zone / healthy-population validated interventions outperform pharmaceutical**  
Interventions validated in Blue Zone, centenarian, or traditional-use population data
(flagged as `healthy_pop_validated=True`) will show higher average adjusted composite
than the pharmaceutical category average. Test: `healthy_pop_avg > pharma_avg`.

---

## 5. Bias Vector Specifications

All 14 bias vectors are defined in `engine/bias_vectors.py`. Each vector describes a
documented, directional, quantifiable distortion in the published evidence base.

### 5.1 Inflation Vectors (inflate apparent pharmaceutical efficacy)

| # | Vector | Direction | Magnitude | Evidence Source |
|---|---|---|---|---|
| 1 | Industry funding inflation | Inflates pharma | Conservative multiplier: 0.35 per industry share (Cochrane OR 3.6) | Bekelman et al JAMA 2003; Lexchin et al BMJ 2003 |
| 2 | Surrogate endpoint inflation | Inflates pharma | Inflation factor: 1.40x | Fleming & DeMets Ann Intern Med 1996; CAST NEJM 1989; ACCORD NEJM 2008 |
| 3 | Publication bias | Inflates pharma | Pharma inflation factor: 1.94x | Turner et al NEJM 2008; Chan et al JAMA 2004; Ross et al BMJ 2009 |
| 4 | Time horizon truncation | Inflates pharma, deflates lifestyle | Short-term inflation: 1.30x | Nature Medicine 2026; Willcox et al (Okinawan dietary transition) |
| 5 | Downstream marker | Inflates pharma | Surrogate failure rate: 0.45 | ACCORD NEJM 2008; ILLUMINATE NEJM 2007; WHI 2002; CAST NEJM 1989 |

### 5.2 Deflation Vectors (deflate apparent non-pharmaceutical efficacy)

| # | Vector | Direction | Magnitude | Evidence Source |
|---|---|---|---|---|
| 6 | No-patent structural underfunding | Deflates natural/lifestyle/terrain | Underfunding discount: 0.70 | Newman & Cragg J Nat Prod 2020; Turner et al JAMA Network Open 2024 |
| 7 | Jurisdictional separation | Deflates oral-systemic | Research gap discount: 0.65 | AHA 2025 Scientific Statement; PAROKRANK Circulation 2016; Cochrane periodontal-diabetes 2022 |
| 8 | Disease population sampling | Deflates lifestyle/natural | Undercount factor: 0.60 | O'Regan & Hirshberg IONS 1993; Gurven et al Lancet 2017 |
| 9 | Adherence undercounting (ITT dilution) | Deflates lifestyle | ITT undercount: 0.55 | Finnish DPS NEJM 2001; Jackevicius et al JAMA 2002 |
| 10 | Outlier responder signal | Deflates natural/terrain/traditional | Correction factor: 1.35x (threshold: responder pct > 2%) | FDA Exceptional Responder Initiative 2017; Othus et al Clin Cancer Res 2012 |
| 11 | Jurisdictional separation (international) | Deflates natural/traditional | Correction factor: 1.20x | PSK Japan approval 1977; Mistletoe EU approvals; WHO 2023 |
| 12 | Bioavailability formulation gap | Deflates natural | Correction factor: 1.25x (trigger: PK validation) | Shoba et al Planta Med 1998 (curcumin +2000% with piperine) |
| 13 | Bradford-Hill mechanistic weight | Deflates natural/traditional | Formula: 1.0 + 0.30 * max(0, (BH - 0.5) / 0.5) | Bradford Hill Proc R Soc Med 1965 |
| 14 | Case series aggregation | Deflates natural/terrain/traditional | Correction factor: 1.15x (threshold: n >= 20) | NCI Exceptional Responder Initiative 2014; WHO evidence framework 2022 |

### 5.3 Additional Vectors Acknowledged But Not Directly Quantified

- **Traditional safety signal:** 1.10x upward correction when continuous use exceeds 200 years (Newman & Cragg 2020; WHO 2023)
- **Evidence grade discount:** Applied universally — A: 1.00, B: 0.88, C: 0.68, D: 0.45

**Note:** The traditional safety signal is implemented in the scoring engine but listed
separately from the 14 primary vectors because it operates as a supplementary correction.

---

## 6. Scoring Model Parameters

### 6.1 Outcome Weights

Bias-corrected composite = SUM(weight_i x raw_outcome_i x bias_multiplier)

| Outcome Dimension | Weight | Rationale |
|---|---|---|
| Mortality (all-cause) | 0.30 | Hardest endpoint; measures what happens to the person |
| Cardiovascular disease | 0.20 | Leading cause of death globally |
| Cancer | 0.18 | Second leading cause of death |
| Metabolic | 0.15 | T2D, insulin resistance, metabolic syndrome |
| Mental health | 0.10 | Depression, cognitive decline, neurodegeneration |
| Whole-system outcome | 0.07 | Disease reversal (not management); categorically different quality of benefit |

**Total: 1.00**

### 6.2 Evidence Grade Discounts

| Grade | Discount Factor |
|---|---|
| A (multiple large RCTs or gold-standard meta-analysis) | 1.00 |
| B (single large RCT, multiple moderate RCTs, or strong meta-analysis) | 0.88 |
| C (small RCTs, large observational, or mechanistic + case series) | 0.68 |
| D (case reports, mechanistic only, traditional use only) | 0.45 |

### 6.3 Correction Model

Corrections are applied **multiplicatively**, not additively. If industry funding
inflates apparent efficacy by 1.35x and publication bias inflates by 1.84x, the
combined inflation is 1.35 x 1.84 = 2.48x, not 3.19x (additive). Multiplicative
models are appropriate when each bias operates on the already-distorted estimate
from prior biases.

---

## 7. Time Horizons

The engine supports three time horizons:

| Horizon | Range | Description |
|---|---|---|
| Short | 1-2 years | Typical RCT duration; favors pharmaceutical (immediate effect) |
| Medium (default) | 5-10 years | Standard comparative window |
| Long | 20+ years / generational | Captures accumulating harm (pharma) and compounding benefit (lifestyle) |

Each intervention record contains `time_horizon_short` and `time_horizon_long`
override values. The medium horizon uses the raw effect size estimates directly.

---

## 8. Key Metrics

### 8.1 Bias Inflation Ratio

`bias_inflation_ratio = raw_composite / adjusted_composite`

- Values > 1.0: the published literature overstates efficacy (typical for pharmaceutical interventions with high industry funding)
- Values < 1.0: the published literature understates efficacy (typical for non-pharmaceutical interventions with structural underfunding)

### 8.2 Number Needed to Treat (NNT)

NNT for all-cause mortality at 10 years is recorded for each intervention from
the published evidence base. This is a direct metric that clinicians and patients
can interpret without requiring statistical training.

---

## 9. Falsifiability

This framework is designed to be falsifiable at multiple levels:

1. **Individual correction factors:** Each bias vector magnitude can be challenged
   with published evidence. If a better meta-analysis establishes a different magnitude,
   the vector is updated and the engine re-run.

2. **Directional hypotheses:** All five hypotheses (Section 4) are pre-specified
   and testable. A result that fails any hypothesis is documented, not suppressed.

3. **New interventions:** Any new intervention can be added to the engine with its
   effect size estimates and bias flags. The engine produces a score. The score can
   be compared to clinical outcomes data as it becomes available.

4. **Retrovalidation (Section 10):** The framework can be applied to historical
   cases where the ground truth is now known.

---

## 10. Proposed Validation Method: Retrovalidation Test

A critical validation of this framework would be retrospective application to
approval-era data for **Vioxx (rofecoxib)** and **Rezulin (troglitazone)**.

If the engine's bias correction model, applied to the published 2000-2004 evidence
base for Vioxx, would have flagged rofecoxib as over-valued (high industry funding,
surrogate endpoint primary outcomes, time horizon truncation, publication bias) and
cardiovascular harm risk, that constitutes falsifiable evidence that the framework
has predictive validity.

Similarly, if applied to Rezulin's approval-era data, the engine should flag
troglitazone as having an inflated efficacy profile due to the same structural biases.

**This retrovalidation test is proposed as an open research question for community
validation.** The engine code, intervention record format, and bias vector definitions
are all public. Any researcher can construct a Vioxx-era intervention record and run
the engine to test whether it would have identified the inflation signal.

---

## 11. Code Repository

All code, data, and correction factors are available at:

**https://github.com/opennnt/bias-corrected-health-engine**

License: MIT  
Language: Python 3.8+  
Dependencies: NumPy  

The repository contains:
- `engine/interventions.py` -- complete intervention library
- `engine/bias_vectors.py` -- 14 bias vector definitions with evidence sources
- `engine/scoring.py` -- multiplicative bias correction and composite scoring
- `engine/run.py` -- CLI entry point
- `METHODOLOGY.md` -- full methodology paper

---

## 12. Associated Preprint

medRxiv (DOI pending -- to be updated after assignment)

Title: "Multi-Vector Bias Correction for Comparative Health Intervention Efficacy:
A Computational Framework Applied to Pharmaceutical vs. Non-Pharmaceutical Chronic
Disease Prevention"

---

## 13. Contact

Eric Chong  
opennnt  
https://github.com/opennnt
