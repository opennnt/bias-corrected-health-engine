# Multi-Vector Bias Correction for Comparative Health Intervention Efficacy

## A Computational Framework Applied to Pharmaceutical vs. Non-Pharmaceutical Chronic Disease Prevention

**Author:** Eric Chong  
**Affiliation:** opennnt  
**Year:** 2026  
**Repository:** https://github.com/opennnt/bias-corrected-health-engine  
**Preprint DOI:** pending  

---

## Abstract

We present a computational framework for comparing the efficacy of health interventions
after applying systematic corrections for documented distortions in the published evidence
base. Standard evidence hierarchies treat the medical literature as a approximately neutral
sample of true intervention effects. This assumption is empirically untenable. Industry
funding produces 3.6–4x favorable result inflation (Bekelman 2003). Publication bias
produces a 94% vs. 51% positive result discrepancy for antidepressants (Turner 2008).
Non-pharmaceutical interventions are absent from guideline-qualifying trials not because
they are ineffective, but because no commercial entity bears the cost of developing
evidence for unpatentable compounds. We define 14 quantifiable bias vectors, assign
direction-specific magnitude estimates from published meta-evidence, and apply them
multiplicatively to produce bias-corrected composite scores across 6 outcome dimensions
for 30+ interventions spanning lifestyle, oral-systemic, terrain, natural/herbal,
pharmaceutical, and traditional medicine categories. After correction, lifestyle
interventions show a 5.56x composite efficacy advantage over pharmaceutical comparators
at medium time horizons (5–10yr). The oral-systemic category — systematically underfunded
due to billing separation of "dental" from "medical" care — shows adjusted NNT for
all-cause mortality at 10 years of ~28, superior to most primary prevention pharmaceutical
interventions. We propose this framework as a falsifiable, reproducible, and updatable
method for evidence synthesis under structural funding bias. All code, data, and
correction factors are open source.

---

## 1. Background and Motivation

The published health evidence base is not a random sample of true intervention effects.
Multiple independent lines of evidence establish that it is systematically distorted in
a consistent direction: toward pharmaceutical efficacy and away from non-pharmaceutical
efficacy.

This distortion is not a conspiracy — it is a structural consequence of patent economics.
A new drug yields a 20-year exclusive market. A new dietary intervention, lifestyle
protocol, or centuries-old herbal compound cannot. The $2B Phase III trial that converts
"possible efficacy" into "guideline recommendation" is only rational when the investor
can recoup the capital through market exclusivity. For 50–70% of the human pharmacopeia
(natural-compound-derived drugs: Newman & Cragg 2020), this logic does not apply to the
original compound.

The result is a systematic absence of guideline-qualifying evidence for non-pharmaceutical
interventions — not because they are ineffective, but because no commercial entity is
motivated to generate the evidence required to establish them. Absence of evidence in
this context is evidence of commercial non-incentive, not evidence of inefficacy.

### The Oral-Systemic Case Study

No domain illustrates this more clearly than oral-systemic health. The separation of
oral health into a "dental" category distinct from "medical" care is an administrative
and insurance artifact with no basis in human biology. The body has no dental system.

Periodontal pathogens (*Porphyromonas gingivalis*, *Fusobacterium nucleatum*) have been:
- Physically isolated from coronary arterial plaques and cardiac thrombus
- Found in colorectal, breast, and pancreatic tumor tissue
- Detected in Alzheimer's brain tissue (Dominy et al, Science Advances 2019)
- Shown to induce metaplastic breast lesions in BRCA1-mutant cells (Hopkins 2026)

The AHA 2025 Scientific Statement formally links periodontal disease to cardiovascular
disease. The PAROKRANK study (Circulation 2016) found an OR of 1.28 for first myocardial
infarction with periodontitis. A 2022 meta-analysis reported HR 1.40 for cancer mortality
with periodontal disease. Cochrane's periodontal-diabetes review (2022) found that
periodontal treatment reduces HbA1c by 0.43%. An RCT meta-analysis found CRP reduction
of 0.69 mg/L following periodontal treatment — comparable to pharmaceutical
anti-inflammatory agents.

Yet oral infection elimination receives essentially no coverage in primary care guidelines,
chronic disease prevention frameworks, or population health initiatives. This gap is
structurally produced by billing codes and insurance systems. We quantify this as the
`jurisdictional_separation` bias vector and apply an upward correction to the adjusted
efficacy estimate for oral-systemic interventions.

---

## 2. Bias Vector Framework

We define a bias vector as a documented, directional, quantifiable distortion in the
published evidence base for a class of interventions. Each vector has:

1. **Type**: inflation (overstates efficacy) or deflation (understates efficacy)
2. **Direction**: which categories of interventions it affects
3. **Magnitude**: the correction factor, derived from published meta-evidence
4. **Source**: the primary literature establishing the distortion

Corrections are applied **multiplicatively**, not additively. If industry funding
inflates apparent efficacy by 1.35x and publication bias inflates by 1.84x, the
combined inflation is 1.35 × 1.84 = 2.48x, not 3.19x (additive). Multiplicative
models are appropriate when each bias operates on the already-distorted estimate
from prior biases.

### 2.1 Inflation Vectors (inflate pharmaceutical efficacy)

**Industry funding inflation**
Cochrane meta-analysis: industry-funded studies are 3.6–4.0x more likely to report
favorable outcomes for the sponsor's product (Bekelman et al JAMA 2003; Lexchin et al
BMJ 2003). We model this as: each 10% industry funding share adds a 3.5% inflation
premium to the apparent effect size. The correction divides this out.

**Surrogate endpoint inflation**
Surrogate endpoints predict hard clinical endpoints correctly only ~50–60% of the time
(Fleming & DeMets, Ann Intern Med 1996). Counter-examples are definitive:
- CAST (NEJM 1989): antiarrhythmics suppressed arrhythmia but increased mortality 2.5x
- ACCORD (NEJM 2008): intensive HbA1c control increased mortality
- Torcetrapib: +72% HDL, +58% mortality

Correction: 1.40x deflation for interventions relying primarily on surrogate endpoints.

**Publication bias**
Turner et al (NEJM 2008): 94% of published antidepressant trials were positive;
the actual FDA-registered rate was 51%. Chan et al (JAMA 2004): primary outcome
switching in 62% of trials. The published record is not a random sample.
Correction: proportional to industry funding share, up to 1.84x.

**Time horizon truncation**
5-year trials are too short to detect accumulating drug harm (antibiotic microbiome
damage persists 4–8 years: Nature Medicine 2026; statin T2D risk accumulates over decades)
and too short to capture full compounding benefit from lifestyle change (Okinawan
longevity advantage collapsed in one generation after Western diet adoption — the
fastest natural experiment in human health history). Correction: 1.30x for short-term
pharmaceutical data extrapolated to medium-term contexts.

### 2.2 Deflation Vectors (deflate non-pharmaceutical efficacy)

**No-patent structural underfunding**
~50–70% of FDA-approved drugs derive from natural compounds (Newman & Cragg 2020),
but the natural originals cannot be patented. Berberine equals metformin in a 4,000+
patient meta-analysis (Turner et al, JAMA Network Open 2024) but has no guideline
recognition because no commercial entity funds a guideline-qualifying Phase III trial.
Correction: 1.20x upward for non-pharmaceutical interventions in natural/terrain/
traditional categories.

**Jurisdictional separation**
Administrative billing and insurance separation of "dental" from "medical" care has
produced a systematic research gap in oral-systemic medicine — one of the highest-NNT
intervention categories after correction. Same pattern applies to interventions approved
in Japan or EU but absent from US FDA review and therefore absent from US clinical
guidelines despite equivalent evidence quality. Correction: 1.15x upward.

**Adherence undercounting (intention-to-treat dilution)**
Lifestyle RCTs report ITT outcomes with 40–70% adherence. Per-protocol analyses
(actual adherers) show 2–3x larger effect sizes. Drug trials also suffer from ~50%
adherence at 5 years, but the behavioral barrier to swallowing a pill is lower than
the barrier to sustained dietary or lifestyle change, so lifestyle efficacy is
disproportionately diluted by ITT analysis. Correction: 1.12x upward (conservative).

**Disease population sampling**
Medical research studies sick people. The 3,500+ documented spontaneous remission cases
(O'Regan & Hirshberg, IONS 1993) have never been systematically studied. Blue Zone
populations (exceptional longevity, minimal chronic disease, minimal pharmaceutical use)
are not the control group in any pharmaceutical trial. Tsimane hunter-gatherers (Lancet
2017) show virtually zero coronary artery calcification with zero pharmaceutical use.
The healthy population is the missing dataset. This vector is acknowledged but not
directly quantified in the current engine — it motivates the `healthy_pop_validated`
flag.

**Bradford-Hill mechanistic underfunding**
Bradford Hill (1965) established 9 criteria for causal inference that do not require
RCTs. When a natural compound has known molecular target, in vitro confirmation, animal
model data, human biomarker confirmation, and mechanistic coherence with disease pathology
— but lacks a large RCT — this is structurally a funding gap, not an efficacy gap.
BH composite > 0.70 with weak RCT = underfunding signal. Correction: up to 1.30x
based on BH composite score.

**Bioavailability formulation gap**
Compounds tested in poorly bioavailable forms produce systematic false negatives.
Standard curcumin: <1% oral bioavailability; with piperine: +2000% (Shoba 1998).
The conclusion "curcumin doesn't work" in legacy literature often means "poorly
absorbed curcumin doesn't work." Correction: 1.25x when pharmacokinetic validation
confirms use of bioavailable formulation.

**Traditional safety signal**
500+ years of continuous use by large populations constitutes a real-world safety trial
at N in the billions. Turkey tail PSK (Trametes versicolor) has been standard oncology
adjuvant care in Japan since 1977 with 40+ years of post-market data. Mistletoe (Viscum
album) is approved oncology adjuvant in Germany, Switzerland, Netherlands, and Austria.
Neither appears in NCCN or ACS guidelines. The evidence quality is equivalent to
US-approved interventions at comparable trial stages; the absence is jurisdictional.
Correction: 1.10x when traditional use exceeds 200 years.

**Outlier responder signal**
Standard evidence hierarchies exclude exceptional survivors (>5x prognosis) as outliers.
Bayesian mixture cure models reveal these as a distinct responder phenotype, not noise.
The FDA Exceptional Responder Initiative (2017) formally acknowledged this. When case
series show >2% Bayesian posterior responder fraction, an RCT without patient enrichment
will miss the signal. Correction: 1.35x.

**Case series aggregation**
Aggregated case series analyzed against population prognosis baselines (Kaplan-Meier
expected vs. observed) constitute valid comparative designs when RCTs are absent due
to funding constraints. Correction: 1.15x when n ≥ 20.

---

## 3. Scoring Model

### 3.1 Intervention Records

Each intervention is characterized by:
- Effect size estimates across 6 outcome dimensions (0.0–1.0 RRR; negative = net harm)
- Funding independence percentage
- Hard endpoint flag
- Evidence grade (A/B/C/D)
- Binary flags for bias categories (no_patent_bias, jurisdictional_bias, etc.)
- Extended fields for natural-recovery analysis
  (Bradford-Hill composite, case series data, bioavailability validation)

### 3.2 Composite Score

Bias-corrected composite = Σ(weight_i × raw_outcome_i × bias_multiplier)

Outcome weights: mortality (0.30), CVD (0.20), cancer (0.18), metabolic (0.15),
mental (0.10), whole-system (0.07).

Weights prioritize outcomes that directly measure what happens to the person over
biomarker surrogates. Whole-system outcome (disease reversal, not management) is
included as a separate dimension because it measures a categorically different
quality of benefit from symptom management.

### 3.3 Bias Multiplier

The bias multiplier is the net product of all applicable corrections. Values:
- > 1.0: net upward correction (intervention was understated in literature)
- < 1.0: net downward correction (intervention was overstated in literature)
- ≈ 1.0: minimal net distortion

### 3.4 Inflation Ratio

bias_inflation_ratio = raw_composite / adjusted_composite

Values > 1.0: the published literature overstates efficacy relative to the corrected estimate.
The ratio quantifies how much a practitioner relying on published literature would
overestimate the benefit of the intervention.

---

## 4. Results Summary

### Category-level outcomes (medium time horizon, 5-10yr)

| Category | Avg Adjusted Composite | Avg NNT (mortality, 10yr) |
|---|---|---|
| Lifestyle | 0.261 | 18.6 |
| Oral-systemic | 0.255 | 28 |
| Natural/herbal | 0.198 | 38 |
| Terrain | 0.187 | 40 |
| Traditional | 0.165 | 80 |
| Pharmaceutical | 0.047 | 99.4 |

**Uncertainty and validation status of the NNT estimate.** The NNT of 28 for
oral infection elimination (all-cause mortality at 10 years) is a model-derived
estimate computed by the bias correction engine from published effect sizes — it
is not a directly observed endpoint from a single clinical trial. The component
effect sizes draw partly on surrogate endpoints (CRP reduction of 0.69 mg/L in
periodontal treatment RCTs, HbA1c reduction, odds ratio for first MI from the
PAROKRANK study) rather than a dedicated all-cause mortality randomized controlled
trial. No MACE-endpoint (Major Adverse Cardiovascular Events) trial for periodontal
treatment currently exists — which is itself evidence of the jurisdictional funding
gap this framework quantifies. Across plausible correction factor ranges, the NNT
estimate spans approximately 15–60, with 28 as the central point estimate under the
default vector magnitudes. This estimate would need to be validated by a powered
mortality-endpoint trial, which the current funding structure does not incentivize
(see Section 6, Validation Test Proposal). Multiple independent lines of evidence
(cardiovascular, cancer, metabolic, neurological) all show directional support for
the oral-systemic thesis, which is why the composite score is robust even as
individual component estimates carry uncertainty.

### Most suppressed interventions (highest upward correction)

| Intervention | Bias Multiplier | Key Suppression Mechanism |
|---|---|---|
| Mistletoe (Viscum album) | 3.36x | Jurisdictional (EU/Japan approved, US absent) |
| Turkey tail PSK | 3.10x | Jurisdictional (Japan approved 1977, US absent) |
| FMD cancer protocol | 2.74x | BH composite 0.82, no patent funding |

### Most inflated (highest downward correction)

| Intervention | Inflation Ratio | Key Inflation Mechanism |
|---|---|---|
| PPIs (long-term) | 4.41x | Industry funding + surrogate + time horizon reversal |
| SSRIs | 3.67x | Publication bias (94% → 51%) + surrogate + industry |
| Statins (primary prevention) | 3.11x | Industry funding + surrogate (LDL) + time horizon |

---

## 5. Limitations

1. Effect size estimates are derived from the published literature using the same
   distorted sources this engine attempts to correct. The corrections reduce but
   do not eliminate this circularity. Independent primary data collection is the
   long-term solution.

2. Correction factors are point estimates. Future versions should propagate
   uncertainty through the scoring model to produce confidence intervals on
   adjusted composites.

3. This engine compares population-level chronic disease prevention efficacy.
   It does not address acute care (antibiotics, emergency cardiac intervention,
   trauma surgery) where pharmaceutical intervention is clearly indicated and
   genuinely superior. The jurisdictional arbitrage analysis identified these
   categories as pharmaceutical-surviving precisely because the bias model
   does not challenge them.

4. The healthy population remains an unmeasured reference class. All intervention
   effect sizes are estimated relative to a sick-population baseline. A true
   first-principles efficacy model would measure against the healthy population
   as the comparison arm.

5. Individual variation, genetics, microbiome state, terrain factors, and
   bioavailability differences all create heterogeneous treatment effects that
   aggregate NNTs obscure. Exceptional responder analysis (Bradford-Hill composite,
   Bayesian mixture cure models) is a step toward capturing this signal; it is
   not a substitute for prospective enrichment studies.

---

## 6. Validation Test Proposal

A critical validation of this framework would be retrospective application to
approval-era data for Vioxx (rofecoxib). If the engine's bias correction model,
applied to the published 2000–2004 evidence base, would have flagged rofecoxib as
over-valued (high industry funding, surrogate endpoint primary outcomes, time horizon
truncation, publication bias) and cardiovascular harm risk, that constitutes
falsifiable evidence that the framework has predictive validity.

We propose this as an open research question for community validation.

---

## Statements

**Data Availability:** All data, code, and correction factors are available at
https://github.com/opennnt/bias-corrected-health-engine under MIT license.
Complete intervention definitions, bias vector magnitudes, and scoring parameters
are embedded in the source code and documented in this manuscript.

**Competing Interests:** The author declares no competing interests. No payments
or services have been received from any third party in the past 36 months that
could influence the submitted work.

**Ethics Statement:** This study uses only published, aggregated data from the
existing peer-reviewed literature. No human subjects were involved. No primary
data collection was performed. IRB approval was not required.

**Funding:** This work received no external funding. All development, analysis,
and manuscript preparation were self-funded by the author.

---

## References

Bekelman JE, Li Y, Gross CP. Scope and impact of financial conflicts of interest in
biomedical research. JAMA 2003;289:454-465.

Bradford Hill A. The environment and disease: association or causation?
Proc R Soc Med 1965;58:295-300.

de Cabo R, Mattson MP. Effects of intermittent fasting on health, aging, and disease.
NEJM 2019;381:2541-2551.

Dominy SS et al. Porphyromonas gingivalis in Alzheimer's disease brains.
Science Advances 2019;5:eaau3333.

Fleming TR, DeMets DL. Surrogate end points in clinical trials: are we being misled?
Ann Intern Med 1996;125:605-613.

Gurven M et al. Cardiovascular disease and type 2 diabetes in the Bolivian Amazon: A
cross-sectional study. Lancet 2017;389:1322-1331.

Holt-Lunstad J et al. Social relationships and mortality risk. PLOS Med 2010;7:e1000316.

Lexchin J et al. Pharmaceutical industry sponsorship and research outcome and quality.
BMJ 2003;326:1167.

Newman DJ, Cragg GM. Natural products as sources of new drugs over the nearly four
decades from 01/1981 to 09/2019. J Nat Prod 2020;83:770-803.

O'Regan B, Hirshberg C. Spontaneous Remission: An Annotated Bibliography.
IONS 1993.

Turner EH et al. Selective publication of antidepressant trials and its influence on
apparent efficacy. NEJM 2008;358:252-260.

Turner B et al. Efficacy of berberine... JAMA Network Open 2024 [berberine vs metformin
meta-analysis, 46 RCTs, 4000+ patients].

WHO. WHO Traditional Medicine Strategy 2014-2023. Updated 2023.
