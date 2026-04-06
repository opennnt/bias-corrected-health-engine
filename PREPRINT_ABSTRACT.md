# Preprint Abstract

**Author:** Eric Chong  
**Affiliation:** opennnt  
**Year:** 2026  
**Repository:** https://github.com/opennnt/bias-corrected-health-engine  
**DOI:** pending

---

## Title

**Multi-Vector Bias Correction for Comparative Health Intervention Efficacy:
A Computational Framework Applied to Pharmaceutical vs. Non-Pharmaceutical
Chronic Disease Prevention**

---

## Abstract (medRxiv / bioRxiv format, ~350 words)

**Background:** Comparative effectiveness research in chronic disease prevention is
systematically distorted by at least four well-documented, quantifiable biases:
industry funding inflation (OR 3.6–4.0: Bekelman 2003), surrogate endpoint over-reliance
(~50–60% predictive accuracy for hard endpoints: Fleming & DeMets 1996), publication bias
(94% vs. 51% positive results for antidepressants: Turner 2008), and structural
underfunding of non-patentable interventions. Standard evidence syntheses do not correct
for these distortions. The resulting comparison — pharmaceutical vs. non-pharmaceutical
chronic disease prevention — is measured on an unlevel playing field.

**Methods:** We define 14 bias vectors with documented direction, magnitude, and evidence
basis. Vectors are applied multiplicatively to raw effect size estimates for 30+
interventions across 6 categories (lifestyle, oral-systemic, terrain, natural/herbal,
pharmaceutical, traditional medicine) and 6 outcome dimensions (all-cause mortality,
CVD, cancer, metabolic, mental, whole-system). We compute bias-corrected composite
scores and NNTs, test 5 pre-specified efficacy hypotheses, and identify time-horizon
reversals. A key methodological contribution is the `jurisdictional_separation` vector,
which quantifies the research gap produced by administrative billing separation of oral
health from systemic medicine — one of the most consequential and structurally produced
gaps in preventive medicine.

**Results:** After bias correction, lifestyle interventions show a 5.56x composite
efficacy advantage over pharmaceutical comparators at 5–10 year horizons (adjusted
composite 0.261 vs. 0.047). Oral infection elimination shows adjusted NNT for all-cause
mortality at 10 years of ~28 — superior to statins for primary CVD prevention (NNT 150),
SSRIs for depression prevention (NNT 200), and aspirin for primary prevention (NNT 250).
This NNT estimate is model-derived from surrogate and composite endpoints (not
a single trial-observed mortality endpoint), spans a plausible range of 15–60
across correction factor sensitivity, and awaits validation by a powered
MACE-endpoint trial that current funding structures do not incentivize.
Whole food diet shows a T2D disease reversal rate of 58% vs. 5% for metformin. Three
interventions are identified as severely suppressed by jurisdictional bias: turkey tail
PSK (Japan-approved since 1977, absent from US guidelines: 3.10x suppressed) and
mistletoe Viscum album (EU-approved oncology adjuvant, absent from US NCCN: 3.36x
suppressed). PPIs, SSRIs, and statins show the largest downward corrections after bias
removal (3.11–4.41x inflation ratios).

**Conclusions:** Standard evidence hierarchies do not correct for structural funding and
publication biases that systematically inflate pharmaceutical and deflate non-pharmaceutical
efficacy estimates. After correction, non-pharmaceutical interventions — particularly
lifestyle modification and oral-systemic care — demonstrate substantially larger
chronic disease prevention effects than pharmaceutical comparators at population level.
The oral-systemic connection in particular represents one of the most underfunded and
highest-impact preventive health domains, with the research gap produced by administrative
rather than biological boundaries. We release the full scoring framework as open-source
software for community review, extension, and validation.

**Keywords:** comparative effectiveness, evidence synthesis, publication bias, industry
funding bias, oral-systemic health, periodontal disease, NNT, lifestyle medicine,
systematic bias correction

---

## Where to Submit

### Primary recommendation: **medRxiv** (medrxiv.org)

**Why medRxiv first, not a journal first:**

1. **Speed of priority establishment.** medRxiv timestamps your priority claim within
   24-48 hours of submission, regardless of peer review timeline. If someone else is
   working on related methodology, your prior art is dated from submission, not
   publication (which can be 12-24 months later for clinical journals).

2. **Indexed immediately by Google Scholar.** Clinicians, researchers, and journalists
   citing your work can find it before peer review completes.

3. **Forces transparency.** A preprint invites public comment. The methodology is either
   defensible or it isn't. Public scrutiny before peer review strengthens the final version.

4. **No embargo on blog/site sharing.** Once on medRxiv you can post it everywhere
   immediately. Traditional journal embargo rules would prevent this.

5. **The methodology is computational and reproducible.** The strongest evidence
   for a computational framework is that the code runs and others can verify the results.
   A GitHub + medRxiv combination does this better than a paywalled PDF.

### Secondary: Submit simultaneously for peer review to:

**Target journal: PLOS Medicine** (open access, high impact, accepts methodological papers,
published the original Kirsch publication bias paper this work cites)

Or: **BMJ Open** (open access, methodological innovation)
Or: **Journal of Clinical Epidemiology** (methods-focused)
Or: **Annals of Internal Medicine** (if you want maximum clinical readership, harder to get)

### What NOT to do:

- Do not submit to a closed-access journal first — the work's leverage is in free
  circulation, not in prestige gating that limits reach
- Do not wait for peer review before posting on GitHub — the code creates independent
  credibility that the preprint can reference
- Do not submit to a journal with pharmaceutical advertising revenue as primary funding
  (most major clinical journals) unless you are comfortable with the dynamics

---

## Submission Sequence

1. **Week 1:** Post code to GitHub (public repo, MIT license)
2. **Week 1:** Post preprint to medRxiv (references the GitHub repo)
3. **Week 1:** Share medRxiv link on your own site with a plain-language summary
4. **Week 2:** Submit to PLOS Medicine for peer review
5. **Month 3–6:** Peer review response with Vioxx/Rezulin retrovalidation as added evidence
6. **On acceptance:** Update GitHub README with published citation

---

## Your Own Site vs. Academia

The question of where to host this has a clear answer: **both, for different purposes**.

**medRxiv + GitHub = the canonical academic record.**
These are the URLs that get cited in papers. They are permanent, indexed, and
institutional-feeling enough that researchers will reference them.

**Your own site = the distribution and context layer.**
A site you control does things medRxiv cannot:
- Plain-language explainer for non-academics (clinicians, patients, journalists)
- Interactive version: "Enter an intervention, see its bias-corrected NNT"
- A place to show the GTFM food index, the oral-systemic research, and the broader
  first-principles health framework in context
- Email list capture — the only way to own your audience rather than renting it
  from an algorithm

**The leverage argument for your own site:**
Academic papers get read by academics. A blog post or tool that goes viral among
functional medicine practitioners, integrative oncologists, or even patients with
a chronic disease gets read by the people who will use the findings and pressure
their providers. These are different audiences requiring different formats.

Recommended site structure:
```
yoursite.com/evidence-engine        — landing page with plain-English summary
yoursite.com/evidence-engine/paper  — embed medRxiv paper or link
yoursite.com/evidence-engine/tool   — interactive NNT lookup (Phase 2)
yoursite.com/oral-systemic          — dedicated page on the dental-is-medical thesis
```

The medRxiv/GitHub combination gives you the academic credibility.
Your own site gives you the distribution.
You need both.
