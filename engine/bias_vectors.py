"""
Bias Vector Definitions
=======================

Each vector describes a systematic distortion in the published health evidence
base, the direction of distortion, the magnitude estimate, which intervention
categories it affects, and the key evidence source.

Vectors are separated from the scoring engine so they can be inspected,
debated, and updated independently of the scoring logic.
"""

BIAS_VECTORS = {

    # -----------------------------------------------------------------------
    # INFLATION VECTORS — inflate apparent efficacy of pharmaceutical agents
    # -----------------------------------------------------------------------

    "industry_funding": {
        "type": "inflation",
        "description": (
            "Industry-funded studies are 3.6–4x more likely to report favorable outcomes "
            "for the sponsor's product. The OR persists across independent meta-analyses. "
            "This inflates apparent pharmaceutical efficacy in the published record."
        ),
        "direction": "inflates_pharma",
        "affects": ["pharmaceutical"],
        "magnitude": {"cochrane_or": 3.6, "conservative_multiplier": 0.35},
        "source": "Bekelman et al JAMA 2003; Lexchin et al BMJ 2003; Cochrane Handbook"
    },

    "surrogate_endpoint": {
        "type": "inflation",
        "description": (
            "Surrogate endpoints predict hard clinical endpoints correctly only ~50–60% "
            "of the time. Counter-examples are definitive: CAST (antiarrhythmics suppressed "
            "arrhythmia, increased mortality 2.5x); ACCORD (intensive HbA1c control "
            "increased mortality); Torcetrapib (+72% HDL, +58% mortality). "
            "Trials using surrogate endpoints systematically overstate benefit."
        ),
        "direction": "inflates_pharma",
        "affects": ["pharmaceutical"],
        "magnitude": {"inflation_factor": 1.40},
        "source": (
            "Fleming & DeMets Ann Intern Med 1996; ACCORD NEJM 2008; CAST NEJM 1989; "
            "Torcetrapib: Nissen et al NEJM 2007"
        )
    },

    "publication_bias": {
        "type": "inflation",
        "description": (
            "Turner et al (NEJM 2008): 94% of published antidepressant trials positive; "
            "actual FDA-registered rate 51%. Chan et al (JAMA 2004): primary outcome "
            "switching in 62% of trials. Ross et al (BMJ 2009): industry trials 60% less "
            "likely to be published within 2 years if results unfavorable. "
            "The published record is not a random sample of all trials conducted."
        ),
        "direction": "inflates_pharma",
        "affects": ["pharmaceutical"],
        "magnitude": {"pharma_inflation_factor": 1.94},
        "source": "Turner et al NEJM 2008; Chan et al JAMA 2004; Ross et al BMJ 2009"
    },

    "time_horizon_truncation": {
        "type": "inflation",
        "description": (
            "Standard RCTs run 3–5 years. This horizon is too short to detect accumulating "
            "harms (antibiotic microbiome damage persists 4–8 years: Nature Medicine 2026; "
            "statin T2D risk accumulates slowly; opioid dependency invisible at 5yr). "
            "It is also too short to capture full benefit compounding from lifestyle change "
            "(Okinawan longevity advantage collapsed in one generation after Western diet "
            "adoption — the fastest natural experiment in human health history). "
            "5yr data systematically inflates pharma and deflates lifestyle."
        ),
        "direction": "inflates_pharma_deflates_lifestyle",
        "affects": ["pharmaceutical"],
        "magnitude": {"short_term_inflation": 1.30},
        "source": (
            "Nature Medicine 2026 (antibiotic microbiome damage, n=14,979); "
            "Willcox et al (Okinawan dietary transition); ACCORD 5yr data"
        )
    },

    "downstream_marker": {
        "type": "inflation",
        "description": (
            "Measuring biomarkers instead of people produces systematic errors. "
            "ACCORD: aggressive HbA1c control → increased mortality. "
            "Torcetrapib: +72% HDL → lethal. HRT: reduced LDL → increased CHD (WHI). "
            "CAST: suppressed arrhythmia → killed patients. "
            "The marker moved in the right direction; the person got worse. "
            "Surrogate marker improvement cannot substitute for hard endpoint data."
        ),
        "direction": "inflates_pharma",
        "affects": ["pharmaceutical"],
        "magnitude": {"surrogate_failure_rate": 0.45},
        "source": (
            "ACCORD NEJM 2008; ILLUMINATE NEJM 2007; WHI 2002; CAST NEJM 1989"
        )
    },

    # -----------------------------------------------------------------------
    # DEFLATION VECTORS — deflate apparent efficacy of non-pharmaceutical agents
    # -----------------------------------------------------------------------

    "no_patent_structural": {
        "type": "deflation",
        "description": (
            "A $2B Phase III trial is only rational if the developer can recoup via patent. "
            "Natural compounds, dietary interventions, and lifestyle modifications cannot be "
            "patented in their native form. ~50–70% of FDA-approved drugs derive from natural "
            "compounds, but the originals are not developed commercially. "
            "Berberine has a 4,000+ patient meta-analysis showing equivalence to metformin "
            "across glycemic, lipid, and metabolic endpoints — but no clinical guideline "
            "recognition because no commercial entity sponsors the guideline-qualifying trial. "
            "Absence of evidence in this context is evidence of commercial non-incentive, "
            "not evidence of inefficacy."
        ),
        "direction": "deflates_natural_lifestyle_terrain",
        "affects": ["natural", "traditional", "lifestyle", "oral_systemic", "terrain"],
        "magnitude": {"underfunding_discount": 0.70},
        "source": (
            "Newman & Cragg J Nat Prod 2020 (~50% approved drugs from natural compounds); "
            "Turner et al JAMA Network Open 2024 (berberine vs metformin, 46 RCTs, 4000+ pts)"
        )
    },

    "jurisdictional_separation": {
        "type": "deflation",
        "description": (
            "The separation of 'dental' from 'medical' is an administrative and insurance "
            "artifact, not a biological one. The human body has no dental system. "
            "Periodontal pathogens (Porphyromonas gingivalis, Fusobacterium nucleatum) "
            "have been physically isolated from arterial plaques, cardiac thrombus, "
            "colorectal tumors, breast tumors, and pancreatic tumors. "
            "AHA 2025 Scientific Statement formally links periodontal disease to CVD. "
            "Periodontal treatment reduces CRP by 0.69 mg/L (RCT meta-analysis) — "
            "comparable to pharmaceutical anti-inflammatory interventions. "
            "The research gap is structurally produced by billing and insurance separation, "
            "not by absence of biological mechanism. Same pattern applies to other "
            "administratively separated fields (e.g., EU/Japan vs FDA jurisdictions for "
            "interventions approved abroad but absent from US guidelines)."
        ),
        "direction": "deflates_oral_systemic",
        "affects": ["oral_systemic"],
        "magnitude": {"research_gap_discount": 0.65},
        "source": (
            "AHA 2025 Scientific Statement on Periodontal Disease and CVD; "
            "PAROKRANK Circulation 2016 (OR 1.28 first MI); "
            "Michaud JAMA (P. gingivalis OR 2.0 pancreatic cancer); "
            "Hopkins 2026 (F. nucleatum → breast metaplasia BRCA1 cells); "
            "RCT meta-analysis PMC 2022 (periodontal tx: CRP −0.69 mg/L); "
            "Cochrane periodontal-diabetes review 2022 (HbA1c −0.43%)"
        )
    },

    "disease_population_sampling": {
        "type": "deflation",
        "description": (
            "Medical research studies sick people in sick-population contexts. "
            "The healthy comparison class is systematically absent. "
            "3,500+ peer-reviewed case reports of cancer/disease remission without "
            "conventional treatment exist (IONS database, O'Regan & Hirshberg 1993); "
            "no major institution has funded a study of what these cases share. "
            "Blue Zone populations (exceptional longevity, minimal chronic disease) "
            "are not used as control groups in pharmaceutical trials. "
            "Tsimane hunter-gatherers (Lancet 2017) show virtually zero coronary artery "
            "calcification at advanced age with zero pharmaceutical use. "
            "Centenarians average 4.8 medications vs 7.0 in the general 75+ population. "
            "The healthy population is the missing dataset."
        ),
        "direction": "deflates_lifestyle_natural",
        "affects": ["lifestyle", "oral_systemic", "terrain", "natural", "traditional"],
        "magnitude": {"undercount_factor": 0.60},
        "source": (
            "O'Regan & Hirshberg IONS 1993 (3500+ spontaneous remission cases); "
            "Gurven et al Lancet 2017 (Tsimane cardiovascular health); "
            "GeroScience 2024 (centenarian polypharmacy review)"
        )
    },

    "adherence_undercounting": {
        "type": "deflation",
        "description": (
            "Lifestyle RCTs typically report intention-to-treat (ITT) outcomes with "
            "40–70% adherence. Per-protocol analyses (actual adherers) show 2–3x larger "
            "effect sizes. Finnish Diabetes Prevention Study: ITT showed 58% T2D risk "
            "reduction; per-protocol was substantially larger. "
            "Drug trials also suffer from ~50% adherence at 5 years, but the behavioral "
            "barrier to taking a pill is lower than the barrier to sustained lifestyle "
            "change, so lifestyle efficacy is more heavily diluted by ITT analysis. "
            "ITT analysis systematically underestimates the biological effect of "
            "lifestyle interventions relative to their pharmaceutical comparators."
        ),
        "direction": "deflates_lifestyle",
        "affects": ["lifestyle", "terrain", "oral_systemic"],
        "magnitude": {"itt_undercount": 0.55},
        "source": (
            "Finnish DPS NEJM 2001 (ITT vs per-protocol T2D risk reduction); "
            "Jackevicius et al JAMA 2002 (medication adherence at 5yr)"
        )
    },

    # -----------------------------------------------------------------------
    # NATURAL-RECOVERY SPECIFIC VECTORS
    # -----------------------------------------------------------------------

    "outlier_responder_signal": {
        "type": "deflation",
        "description": (
            "Standard evidence hierarchies treat exceptional survivors (those exceeding "
            "prognosis by >5x) as statistical outliers to be excluded or dismissed. "
            "Bayesian mixture cure models reveal these as a distinct responder phenotype, "
            "not noise. The FDA Exceptional Responder Initiative (2017) formally acknowledged "
            "this phenomenon and recommended prospective enrichment strategies. "
            "When case series show >2% Bayesian posterior responder fraction, the "
            "intervention has a real signal that underpowered RCTs without patient "
            "enrichment will fail to detect. Upward correction of 1.35x applied when "
            "case_series_bayesian_responder_pct > 0.02."
        ),
        "direction": "deflates_natural",
        "affects": ["natural", "terrain", "traditional"],
        "magnitude": {"correction_factor": 1.35, "responder_pct_threshold": 0.02},
        "source": (
            "FDA Exceptional Responder Initiative 2017; "
            "Othus et al Clin Cancer Res 2012 (Bayesian mixture cure models); "
            "IONS spontaneous remission database (3500+ cases)"
        )
    },

    "jurisdictional_separation_bias": {
        "type": "deflation",
        "description": (
            "Interventions approved in Japan or EU but not by the FDA receive effectively "
            "zero coverage in US clinical literature, guidelines, and medical education. "
            "PSK (Trametes versicolor / turkey tail) has been approved in Japan since 1977 "
            "as a cancer adjuvant for gastric, colorectal, and lung cancer, with 40+ years "
            "of post-market data. Mistletoe (Viscum album, Iscador) is approved and "
            "routinely used as oncology adjuvant in Germany, Switzerland, Netherlands, "
            "and Austria, with 26 controlled studies and multiple meta-analyses. "
            "Neither intervention appears in NCCN or ACS guidelines. "
            "The evidence quality is equivalent to approved US interventions at comparable "
            "trial stages; the absence is jurisdictional, not scientific."
        ),
        "direction": "deflates_natural_traditional",
        "affects": ["natural", "traditional"],
        "magnitude": {"correction_factor": 1.20},
        "source": (
            "PSK: Ohwada et al Anticancer Res 2004; Japan Ministry of Health approval 1977; "
            "Mistletoe: Kienle & Kiene Altern Ther Health Med 2007 (26 studies); "
            "WHO 2023 traditional medicine strategy"
        )
    },

    "bioavailability_formulation_gap": {
        "type": "deflation",
        "description": (
            "Natural compounds tested in poorly bioavailable forms produce systematic "
            "false negatives that then dominate the literature. "
            "Standard curcumin: <1% oral bioavailability; with piperine: +2000% "
            "(Shoba 1998). Resveratrol undergoes rapid hepatic conjugation; liposomal "
            "formulations show radically different pharmacokinetics. Berberine has "
            "low baseline oral bioavailability substantially improved by dihydroberberine "
            "or nanoformulation. The conclusion 'curcumin doesn't work' in the literature "
            "often reflects 'unenhanced curcumin at <1% bioavailability doesn't work' — "
            "a formulation artifact, not a compound failure. Upward correction 1.25x when "
            "pharmacokinetic_validation=True (intervention tested in validated form)."
        ),
        "direction": "deflates_natural",
        "affects": ["natural"],
        "magnitude": {"correction_factor": 1.25, "trigger": "pharmacokinetic_validation"},
        "source": (
            "Shoba et al Planta Med 1998 (curcumin + piperine: +2000% bioavailability); "
            "Turner et al JAMA Network Open 2024 (berberine formulation differences); "
            "van Breemen & Bhanu 2011 J Pharm Sci (general bioavailability review)"
        )
    },

    "bradford_hill_mechanistic_weight": {
        "type": "deflation",
        "description": (
            "Bradford Hill (1965) established 9 criteria for causal inference that do not "
            "require RCTs: strength, consistency, specificity, temporality, biological "
            "gradient, plausibility, coherence, experiment, analogy. "
            "When a natural compound has: (1) known molecular target, (2) in vitro "
            "confirmation, (3) animal model data, (4) human biomarker confirmation, "
            "and (5) mechanistic coherence with disease pathology — but lacks a large RCT — "
            "this structural pattern is a funding gap signal, not an efficacy gap signal. "
            "Bradford Hill composite >0.7 with weak or absent RCT = underfunding by design. "
            "Correction up to 1.30x based on BH composite score."
        ),
        "direction": "deflates_natural_traditional",
        "affects": ["natural", "terrain", "traditional"],
        "magnitude": {"correction_formula": "1.0 + 0.30 * max(0, (bh_composite - 0.5) / 0.5)"},
        "source": (
            "Bradford Hill Proc R Soc Med 1965; "
            "Rothman & Greenland 2005 (epidemiologic methods); "
            "Illari & Williamson 2012 (mechanistic evidence in causal inference)"
        )
    },

    "case_series_aggregation": {
        "type": "deflation",
        "description": (
            "Single-institution case series are systematically dismissed in evidence "
            "hierarchies despite containing valid comparative signal when aggregated "
            "against population prognosis baselines. Kaplan-Meier expected vs observed "
            "survival analysis against matched historical controls constitutes a valid "
            "comparative design when RCTs are absent due to funding gaps (not lack of "
            "mechanism). WHO evidence framework 2022 explicitly recognizes aggregated "
            "case series as admissible evidence in under-resourced research areas. "
            "Correction 1.15x when case_series_n >= 20."
        ),
        "direction": "deflates_natural_traditional",
        "affects": ["natural", "terrain", "traditional"],
        "magnitude": {"correction_factor": 1.15, "threshold_n": 20},
        "source": (
            "NCI Exceptional Responder Initiative 2014; "
            "Wittes et al Stat Med 1989 (aggregated case series methodology); "
            "WHO evidence framework 2022"
        )
    },

    "traditional_safety_signal": {
        "type": "deflation",
        "description": (
            "Centuries of continuous use in large populations constitutes a real-world "
            "safety dataset that modern regulatory systems cannot replicate at equivalent "
            "scale. A compound in continuous use by hundreds of millions of people over "
            "500+ years has an implicit N in the billions for safety outcomes, and an "
            "implicit observational efficacy signal through survival of the practice. "
            "80% of the world's population currently uses traditional medicine as primary "
            "care (WHO 2023). 50–70% of FDA-approved drugs derive from natural compounds. "
            "Correction 1.10x when population_safety_signal_years > 200."
        ),
        "direction": "deflates_traditional",
        "affects": ["natural", "traditional"],
        "magnitude": {"correction_factor": 1.10, "threshold_years": 200},
        "source": (
            "WHO traditional medicine report 2023; "
            "Newman & Cragg J Nat Prod 2020 (natural compounds in drug approvals)"
        )
    },
}
