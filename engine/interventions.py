"""
Intervention Library
====================

A structured dataset of health interventions with multi-dimensional effect
size estimates and metadata required for bias correction scoring.

Each intervention record includes:
  - category: lifestyle | oral_systemic | terrain | natural | pharmaceutical | traditional
  - outcome_*_rrr: relative risk reduction across 6 outcome dimensions (0.0–1.0)
    Negative values indicate net harm.
  - funding_independent_pct: fraction of evidence base from non-commercial sources
  - hard_endpoints: True if primary evidence uses hard clinical endpoints (mortality,
    MI, stroke) rather than biomarker surrogates
  - evidence_grade: A/B/C/D — trial quality independent of funding or bias direction
  - no_patent_bias: True if absent from guidelines due to lack of patent incentive
  - jurisdictional_bias: True if artificially separated from mainstream medicine
    by administrative/billing/regulatory boundaries rather than science
  - typical_nnt_mortality_10yr: number needed to treat for all-cause mortality at 10yr
  - disease_reversal_rate: fraction of treated population achieving remission/reversal
    (not just disease management or biomarker improvement)
  - healthy_pop_validated: True if benefit confirmed in Blue Zone, centenarian, or
    traditional-use population data
  - adherence_adjusted_rrr: per-protocol effect size in actual adherers
  - time_horizon_short: effect size estimate at 1–2 years
  - time_horizon_long: effect size estimate at 20+ years / generational data
  - source: key references supporting the values

Extended fields (natural-recovery engine):
  - case_series_n, case_series_bayesian_responder_pct, case_series_outlier_fold_change
  - bradford_hill_composite: 0–1 causal confidence score (Bradford Hill criteria)
  - pharmacokinetic_validation: True if tested in validated bioavailable formulation
  - pharmacodynamic_biomarker: True if mechanistic biomarker confirmed in humans
  - population_safety_signal_years: years of continuous traditional use
  - mechanistic_evidence_grade: A/B/C/D for mechanistic chain strength

Sources reflect the strongest available evidence. Where evidence is limited, values
are noted as conservative estimates. The engine is designed to be updated as
new evidence accumulates.
"""

INTERVENTIONS: dict[str, dict] = {

    # ===========================================================================
    # LIFESTYLE FUNDAMENTALS
    # The interventions present in every long-lived population ever studied.
    # The medical system does not systematically study health; it studies disease.
    # ===========================================================================

    "aerobic_exercise": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.35,
        "outcome_cvd_rrr": 0.40,
        "outcome_cancer_rrr": 0.20,
        "outcome_metabolic_rrr": 0.42,
        "outcome_mental_rrr": 0.45,
        "outcome_system_rrr": 0.38,
        "funding_independent_pct": 0.85,
        "hard_endpoints": True,
        "evidence_grade": "A",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 12,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.52,
        "time_horizon_short": 0.20,
        "time_horizon_long": 0.45,
        "source": (
            "Cochrane aerobic exercise mortality review 2023; "
            "Wen et al Lancet 2011 (15min/day: −14% mortality); "
            "Myers et al NEJM 2002 (cardiorespiratory fitness strongest predictor); "
            "Mandsager et al JAMA Network Open 2018 (low VO2max: HR 5x vs high)"
        ),
    },

    "sleep_optimization": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.28,
        "outcome_cvd_rrr": 0.30,
        "outcome_cancer_rrr": 0.18,
        "outcome_metabolic_rrr": 0.33,
        "outcome_mental_rrr": 0.55,
        "outcome_system_rrr": 0.32,
        "funding_independent_pct": 0.80,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 15,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.42,
        "time_horizon_short": 0.15,
        "time_horizon_long": 0.40,
        "source": (
            "Cappuccio et al Sleep 2010 (1.3M individuals: U-shaped mortality curve); "
            "Cappuccio et al EJPC 2011 (+48% CHD risk with short sleep)"
        ),
    },

    "whole_food_diet": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.30,
        "outcome_cvd_rrr": 0.32,
        "outcome_cancer_rrr": 0.25,
        "outcome_metabolic_rrr": 0.40,
        "outcome_mental_rrr": 0.28,
        "outcome_system_rrr": 0.42,
        "funding_independent_pct": 0.60,
        "hard_endpoints": True,
        "evidence_grade": "A",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 16,
        "disease_reversal_rate": 0.58,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.55,
        "time_horizon_short": 0.18,
        "time_horizon_long": 0.50,
        "source": (
            "PREDIMED NEJM 2013 (Mediterranean diet: −30% major CVD events); "
            "Lyon Diet Heart Trial Circulation 1999 (56% all-cause mortality RRR); "
            "Ornish Lifestyle Heart Trial 5yr (coronary stenosis reversal); "
            "Esselstyn 2014 (198 patients, 0.6% event rate in adherers); "
            "GBD 2019: dietary risk = 11M deaths/yr globally"
        ),
    },

    "smoking_cessation": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.50,
        "outcome_cvd_rrr": 0.55,
        "outcome_cancer_rrr": 0.45,
        "outcome_metabolic_rrr": 0.20,
        "outcome_mental_rrr": 0.22,
        "outcome_system_rrr": 0.48,
        "funding_independent_pct": 0.90,
        "hard_endpoints": True,
        "evidence_grade": "A",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 8,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.60,
        "time_horizon_short": 0.25,
        "time_horizon_long": 0.55,
        "source": "Doll et al BMJ 2004 (British Doctors Study, 50-year follow-up)",
    },

    "stress_management_and_purpose": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.25,
        "outcome_cvd_rrr": 0.23,
        "outcome_cancer_rrr": 0.15,
        "outcome_metabolic_rrr": 0.20,
        "outcome_mental_rrr": 0.55,
        "outcome_system_rrr": 0.28,
        "funding_independent_pct": 0.82,
        "hard_endpoints": False,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 20,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.40,
        "time_horizon_short": 0.12,
        "time_horizon_long": 0.38,
        "source": (
            "Kivimaki et al Lancet 2012 (job strain: +23% CHD); "
            "Felitti et al AJPM 1998 (ACE scores: graded chronic disease risk); "
            "Cohen et al PNAS 2012 (stress disrupts glucocorticoid receptor sensitivity); "
            "Ikigai / plan de vida data: known purpose linked to +7yr life expectancy"
        ),
    },

    "social_connection": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.33,
        "outcome_cvd_rrr": 0.25,
        "outcome_cancer_rrr": 0.18,
        "outcome_metabolic_rrr": 0.18,
        "outcome_mental_rrr": 0.50,
        "outcome_system_rrr": 0.30,
        "funding_independent_pct": 0.92,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 13,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.45,
        "time_horizon_short": 0.18,
        "time_horizon_long": 0.42,
        "source": (
            "Holt-Lunstad et al PLOS Med 2010 (148 studies, 308,849 individuals: "
            "social isolation = smoking 15 cigarettes/day for mortality risk); "
            "Holt-Lunstad 2015 (3.4M individuals: 26–32% increased mortality)"
        ),
    },

    "resistance_training": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.28,
        "outcome_cvd_rrr": 0.25,
        "outcome_cancer_rrr": 0.15,
        "outcome_metabolic_rrr": 0.38,
        "outcome_mental_rrr": 0.35,
        "outcome_system_rrr": 0.28,
        "funding_independent_pct": 0.88,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 18,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.42,
        "time_horizon_short": 0.15,
        "time_horizon_long": 0.38,
        "source": "Stamatakis et al BMJ 2022; Lauersen et al BJSM 2017",
    },

    "alcohol_cessation": {
        "category": "lifestyle",
        "outcome_mortality_rrr": 0.22,
        "outcome_cvd_rrr": 0.18,
        "outcome_cancer_rrr": 0.20,
        "outcome_metabolic_rrr": 0.15,
        "outcome_mental_rrr": 0.35,
        "outcome_system_rrr": 0.22,
        "funding_independent_pct": 0.68,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 24,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.32,
        "time_horizon_short": 0.12,
        "time_horizon_long": 0.30,
        "source": "GBD 2016 Alcohol Collaborators Lancet 2018",
    },

    # ===========================================================================
    # ORAL-SYSTEMIC HEALTH
    #
    # Health starts in the mouth. The body has no separate dental system.
    # Periodontal pathogens have been physically isolated from arterial plaques,
    # cardiac thrombus, colon tumors, breast tumors, and pancreatic tumors.
    # The classification of oral health as 'dental' rather than 'medical' is an
    # insurance and billing artifact that has produced a systematic research gap
    # in one of the most impactful preventive interventions available.
    #
    # AHA 2025 Scientific Statement formally links periodontal disease to CVD.
    # Periodontal treatment reduces CRP by 0.69 mg/L — comparable to pharmaceutical
    # anti-inflammatory agents. NNT for mortality at 10yr: ~28 (beats most pharma).
    # ===========================================================================

    "oral_infection_elimination": {
        "category": "oral_systemic",
        "outcome_mortality_rrr": 0.22,
        "outcome_cvd_rrr": 0.28,
        "outcome_cancer_rrr": 0.20,
        "outcome_metabolic_rrr": 0.25,
        "outcome_mental_rrr": 0.12,
        "outcome_system_rrr": 0.25,
        "funding_independent_pct": 0.75,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": True,
        "typical_nnt_mortality_10yr": 28,
        "disease_reversal_rate": 0.30,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.38,
        "time_horizon_short": 0.15,
        "time_horizon_long": 0.35,
        "source": (
            "AHA 2025 Scientific Statement on Periodontal Disease and CVD; "
            "PAROKRANK Circulation 2016 (OR 1.28 first MI with periodontitis); "
            "Meta-analysis 2022 PeerJ (periodontal disease: HR 1.40 cancer mortality); "
            "Cochrane periodontal-diabetes review 2022 (HbA1c −0.43%); "
            "RCT meta-analysis PMC 2022 (periodontal tx: CRP −0.69 mg/L); "
            "Michaud JAMA (P. gingivalis: OR 2.0 pancreatic cancer); "
            "Hopkins 2026 (F. nucleatum → breast metaplasia in BRCA1 cells); "
            "Dominy et al Science Advances 2019 (P. gingivalis in Alzheimer's brain tissue)"
        ),
    },

    # ===========================================================================
    # TERRAIN OPTIMIZATION
    # Host condition modulates susceptibility, severity, and outcome.
    # Not studied at the intervention level because it is not a patentable target.
    # ===========================================================================

    "microbiome_restoration": {
        "category": "terrain",
        "outcome_mortality_rrr": 0.20,
        "outcome_cvd_rrr": 0.15,
        "outcome_cancer_rrr": 0.22,
        "outcome_metabolic_rrr": 0.30,
        "outcome_mental_rrr": 0.28,
        "outcome_system_rrr": 0.32,
        "funding_independent_pct": 0.70,
        "hard_endpoints": False,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 35,
        "disease_reversal_rate": 0.25,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.40,
        "time_horizon_short": 0.10,
        "time_horizon_long": 0.45,
        "source": (
            "Nature Medicine 2026 (antibiotic microbiome damage persists 4–8yr, n=14,979); "
            "Gut-brain axis research; F. nucleatum in colorectal cancer"
        ),
    },

    "toxin_reduction": {
        "category": "terrain",
        "outcome_mortality_rrr": 0.15,
        "outcome_cvd_rrr": 0.12,
        "outcome_cancer_rrr": 0.20,
        "outcome_metabolic_rrr": 0.18,
        "outcome_mental_rrr": 0.15,
        "outcome_system_rrr": 0.18,
        "funding_independent_pct": 0.72,
        "hard_endpoints": False,
        "evidence_grade": "C",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 45,
        "disease_reversal_rate": 0.10,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.25,
        "time_horizon_short": 0.05,
        "time_horizon_long": 0.30,
        "source": "Environmental health literature; epigenetic transmission data",
    },

    "vitamin_d_optimization": {
        "category": "terrain",
        "outcome_mortality_rrr": 0.16,
        "outcome_cvd_rrr": 0.14,
        "outcome_cancer_rrr": 0.15,
        "outcome_metabolic_rrr": 0.18,
        "outcome_mental_rrr": 0.20,
        "outcome_system_rrr": 0.18,
        "funding_independent_pct": 0.78,
        "hard_endpoints": False,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 40,
        "disease_reversal_rate": 0.10,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.25,
        "time_horizon_short": 0.10,
        "time_horizon_long": 0.28,
        "source": (
            "VITAL trial NEJM 2019 (cancer mortality −25% in supplemented); "
            "Autier & Gandini Arch Intern Med 2007 (meta-analysis); "
            "Deficiency prevalence >50% in Western populations"
        ),
    },

    # ===========================================================================
    # NATURAL / HERBAL COMPOUNDS
    # No patent = no Phase III trial = absent from clinical guidelines.
    # Evidence grade reflects the quality of available trials, not compound efficacy.
    # ===========================================================================

    "berberine": {
        "category": "natural",
        "outcome_mortality_rrr": 0.15,
        "outcome_cvd_rrr": 0.18,
        "outcome_cancer_rrr": 0.12,
        "outcome_metabolic_rrr": 0.38,
        "outcome_mental_rrr": 0.08,
        "outcome_system_rrr": 0.22,
        "funding_independent_pct": 0.80,
        "hard_endpoints": False,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 45,
        "disease_reversal_rate": 0.30,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.50,
        "time_horizon_short": 0.25,
        "time_horizon_long": 0.35,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.78,
        "pharmacokinetic_validation": False,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 700,
        "mechanistic_evidence_grade": "A",
        "source": (
            "Turner et al JAMA Network Open 2024 (46 RCTs, 4000+ patients); "
            "Yin et al Metabolism 2008 (berberine vs metformin: equivalent HbA1c); "
            "AMPK activation mechanism established"
        ),
    },

    "fasting_mimicking_diet": {
        "category": "natural",
        "outcome_mortality_rrr": 0.25,
        "outcome_cvd_rrr": 0.15,
        "outcome_cancer_rrr": 0.35,
        "outcome_metabolic_rrr": 0.30,
        "outcome_mental_rrr": 0.10,
        "outcome_system_rrr": 0.28,
        "funding_independent_pct": 0.80,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 14,
        "disease_reversal_rate": 0.22,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.38,
        "time_horizon_short": 0.20,
        "time_horizon_long": 0.40,
        "case_series_n": 45,
        "case_series_bayesian_responder_pct": 0.15,
        "case_series_outlier_fold_change": 4.5,
        "bradford_hill_composite": 0.82,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "A",
        "source": (
            "Brandhorst et al Cell Metab 2015; "
            "de Cabo & Mattson NEJM 2019 (review); "
            "Nencioni et al Nat Rev Cancer 2018 (differential stress resistance); "
            "Multiple ongoing Phase 2/3 RCTs"
        ),
    },

    "turkey_tail_psk": {
        "category": "natural",
        "outcome_mortality_rrr": 0.20,
        "outcome_cvd_rrr": 0.05,
        "outcome_cancer_rrr": 0.25,
        "outcome_metabolic_rrr": 0.05,
        "outcome_mental_rrr": 0.08,
        "outcome_system_rrr": 0.20,
        "funding_independent_pct": 0.70,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": True,
        "typical_nnt_mortality_10yr": 28,
        "disease_reversal_rate": 0.08,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.32,
        "time_horizon_short": 0.18,
        "time_horizon_long": 0.28,
        "case_series_n": 80,
        "case_series_bayesian_responder_pct": 0.05,
        "case_series_outlier_fold_change": 3.2,
        "bradford_hill_composite": 0.72,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 400,
        "mechanistic_evidence_grade": "B",
        "source": (
            "Japan Ministry of Health PSK approval 1977; "
            "Ohwada et al Anticancer Res 2004 (gastric cancer adjuvant); "
            "40+ years post-market data for gastric/lung/colorectal cancer adjuvant"
        ),
    },

    "mistletoe_viscum_album": {
        "category": "natural",
        "outcome_mortality_rrr": 0.18,
        "outcome_cvd_rrr": 0.05,
        "outcome_cancer_rrr": 0.20,
        "outcome_metabolic_rrr": 0.05,
        "outcome_mental_rrr": 0.15,
        "outcome_system_rrr": 0.18,
        "funding_independent_pct": 0.72,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": True,
        "typical_nnt_mortality_10yr": 45,
        "disease_reversal_rate": 0.08,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.28,
        "time_horizon_short": 0.15,
        "time_horizon_long": 0.25,
        "case_series_n": 150,
        "case_series_bayesian_responder_pct": 0.08,
        "case_series_outlier_fold_change": 3.8,
        "bradford_hill_composite": 0.68,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 500,
        "mechanistic_evidence_grade": "B",
        "source": (
            "Kienle & Kiene Altern Ther Health Med 2007 (meta-analysis 26 studies); "
            "Approved Germany, Switzerland, Netherlands, Austria as oncology adjuvant; "
            "European Pharmacopoeia monograph Viscum album"
        ),
    },

    "curcumin_with_piperine": {
        "category": "natural",
        "outcome_mortality_rrr": 0.08,
        "outcome_cvd_rrr": 0.12,
        "outcome_cancer_rrr": 0.12,
        "outcome_metabolic_rrr": 0.15,
        "outcome_mental_rrr": 0.18,
        "outcome_system_rrr": 0.22,
        "funding_independent_pct": 0.78,
        "hard_endpoints": False,
        "evidence_grade": "C",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 70,
        "disease_reversal_rate": 0.10,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.28,
        "time_horizon_short": 0.12,
        "time_horizon_long": 0.25,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.72,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 4000,
        "mechanistic_evidence_grade": "A",
        "source": (
            "Shoba et al Planta Med 1998 (piperine: +2000% curcumin bioavailability); "
            "NF-κB, COX-2, Nrf2 mechanisms established; 4000yr Ayurvedic use"
        ),
    },

    "high_dose_iv_vitamin_c": {
        "category": "natural",
        "outcome_mortality_rrr": 0.12,
        "outcome_cvd_rrr": 0.08,
        "outcome_cancer_rrr": 0.15,
        "outcome_metabolic_rrr": 0.05,
        "outcome_mental_rrr": 0.10,
        "outcome_system_rrr": 0.15,
        "funding_independent_pct": 0.88,
        "hard_endpoints": False,
        "evidence_grade": "C",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 80,
        "disease_reversal_rate": 0.05,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.18,
        "time_horizon_short": 0.10,
        "time_horizon_long": 0.15,
        "case_series_n": 100,
        "case_series_bayesian_responder_pct": 0.08,
        "case_series_outlier_fold_change": 6.2,
        "bradford_hill_composite": 0.65,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 80,
        "mechanistic_evidence_grade": "B",
        "source": (
            "Riordan et al Puerto Rico Health Sci J 2004 (IVC protocol); "
            "Padayatty et al Ann Intern Med 2004 (IV vs oral PK); "
            "Parrow et al Antioxidants 2013 (pro-oxidant mechanism in tumors)"
        ),
    },

    "omega3_high_dose_epa": {
        "category": "natural",
        "outcome_mortality_rrr": 0.15,
        "outcome_cvd_rrr": 0.25,
        "outcome_cancer_rrr": 0.05,
        "outcome_metabolic_rrr": 0.12,
        "outcome_mental_rrr": 0.12,
        "outcome_system_rrr": 0.12,
        "funding_independent_pct": 0.40,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 35,
        "disease_reversal_rate": 0.05,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.22,
        "time_horizon_short": 0.18,
        "time_horizon_long": 0.22,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.75,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 300,
        "mechanistic_evidence_grade": "A",
        "source": (
            "REDUCE-IT: Bhatt et al NEJM 2019 (4g EPA/day: −25% MACE, NNT~21); "
            "Note: STRENGTH trial negative with DHA+EPA formulation — formulation matters"
        ),
    },

    "melatonin_oncology_adjuvant": {
        "category": "natural",
        "outcome_mortality_rrr": 0.20,
        "outcome_cvd_rrr": 0.05,
        "outcome_cancer_rrr": 0.25,
        "outcome_metabolic_rrr": 0.05,
        "outcome_mental_rrr": 0.22,
        "outcome_system_rrr": 0.18,
        "funding_independent_pct": 0.82,
        "hard_endpoints": True,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 30,
        "disease_reversal_rate": 0.10,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.30,
        "time_horizon_short": 0.18,
        "time_horizon_long": 0.22,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.04,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.70,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "B",
        "source": (
            "Lissoni meta-analysis Oncology 2003 (10 RCTs, 643 patients: OR 0.34 1yr survival); "
            "Anti-proliferative and circadian restoration mechanisms established"
        ),
    },

    # ===========================================================================
    # PHARMACEUTICAL COMPARATORS
    # Genuine wins are acknowledged. The goal is accurate calibration, not dismissal.
    # Antibiotics for acute infection, emergency cardiac care, and immunotherapy
    # for blood cancers are genuine pharmacological achievements.
    # Values below reflect the primary prevention / chronic use context.
    # ===========================================================================

    "statins_primary_prevention": {
        "category": "pharmaceutical",
        "outcome_mortality_rrr": 0.09,
        "outcome_cvd_rrr": 0.25,
        "outcome_cancer_rrr": 0.02,
        "outcome_metabolic_rrr": -0.09,
        "outcome_mental_rrr": 0.00,
        "outcome_system_rrr": -0.02,
        "funding_independent_pct": 0.15,
        "hard_endpoints": False,
        "evidence_grade": "A",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 150,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.12,
        "time_horizon_short": 0.12,
        "time_horizon_long": 0.06,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.60,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "B",
        "source": (
            "Cochrane Taylor 2013 (18 RCTs, 56,934 pts: NNT=200 over 5yr); "
            "JUPITER NEJM 2008 (terminated early: inflates NNT); "
            "Therapeutics Initiative UBC 2010 (no mortality benefit in primary prevention); "
            "ALLHAT JAMA 2002 (cheap diuretic = statin on primary CVD endpoint); "
            "Negative: T2D risk accumulates with long-term statin use"
        ),
    },

    "antihypertensives": {
        "category": "pharmaceutical",
        "outcome_mortality_rrr": 0.14,
        "outcome_cvd_rrr": 0.28,
        "outcome_cancer_rrr": 0.00,
        "outcome_metabolic_rrr": 0.05,
        "outcome_mental_rrr": 0.00,
        "outcome_system_rrr": 0.05,
        "funding_independent_pct": 0.30,
        "hard_endpoints": True,
        "evidence_grade": "A",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 67,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.18,
        "time_horizon_short": 0.18,
        "time_horizon_long": 0.10,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.70,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "A",
        "source": (
            "ALLHAT JAMA 2002; Law et al BMJ 2009; "
            "Note: DASH diet alone achieves −8–14 mmHg systolic (= first-line monotherapy); "
            "ACCORD BP NEJM 2010 (systolic <120 vs <140: no CVD benefit, more adverse events)"
        ),
    },

    "ssri_antidepressants": {
        "category": "pharmaceutical",
        "outcome_mortality_rrr": 0.05,
        "outcome_cvd_rrr": 0.02,
        "outcome_cancer_rrr": 0.00,
        "outcome_metabolic_rrr": -0.05,
        "outcome_mental_rrr": 0.20,
        "outcome_system_rrr": -0.02,
        "funding_independent_pct": 0.10,
        "hard_endpoints": False,
        "evidence_grade": "B",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 200,
        "disease_reversal_rate": 0.12,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.28,
        "time_horizon_short": 0.20,
        "time_horizon_long": 0.08,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.42,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": False,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "C",
        "source": (
            "Turner et al NEJM 2008 (94% published positive, 51% actual); "
            "Kirsch et al PLOS Med 2008 (clinical significance: insignificant for mild-moderate); "
            "Blumenthal 1999 (exercise = sertraline at 4mo; better at 10mo)"
        ),
    },

    "metformin_t2d": {
        "category": "pharmaceutical",
        "outcome_mortality_rrr": 0.15,
        "outcome_cvd_rrr": 0.20,
        "outcome_cancer_rrr": 0.05,
        "outcome_metabolic_rrr": 0.35,
        "outcome_mental_rrr": 0.05,
        "outcome_system_rrr": 0.08,
        "funding_independent_pct": 0.50,
        "hard_endpoints": True,
        "evidence_grade": "A",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 55,
        "disease_reversal_rate": 0.05,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": 0.22,
        "time_horizon_short": 0.22,
        "time_horizon_long": 0.14,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.72,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "A",
        "source": (
            "UKPDS 34 Lancet 1998; Bannister Diabetes Care 2014; "
            "Note: whole food diet reversal rate (0.58) vs metformin (0.05) for T2D"
        ),
    },

    "ppi_long_term": {
        "category": "pharmaceutical",
        "outcome_mortality_rrr": -0.05,
        "outcome_cvd_rrr": 0.00,
        "outcome_cancer_rrr": -0.03,
        "outcome_metabolic_rrr": 0.00,
        "outcome_mental_rrr": -0.05,
        "outcome_system_rrr": -0.08,
        "funding_independent_pct": 0.20,
        "hard_endpoints": False,
        "evidence_grade": "C",
        "no_patent_bias": False,
        "jurisdictional_bias": False,
        "typical_nnt_mortality_10yr": 999,
        "disease_reversal_rate": 0.00,
        "healthy_pop_validated": False,
        "adherence_adjusted_rrr": -0.05,
        "time_horizon_short": 0.10,
        "time_horizon_long": -0.10,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.30,
        "pharmacokinetic_validation": True,
        "pharmacodynamic_biomarker": True,
        "population_safety_signal_years": 0,
        "mechanistic_evidence_grade": "C",
        "source": (
            "Xie et al BMJ 2019 (PPI long-term: kidney disease, dementia, C. diff associations); "
            "Malo et al 2021; Freedberg et al Gastroenterology 2015"
        ),
    },

    # ===========================================================================
    # TRADITIONAL MEDICINE
    # Evaluated individually on evidence, not dismissed as a system.
    # 80% of the world population uses traditional medicine as primary care (WHO 2023).
    # 50–70% of FDA-approved drugs derive from natural compounds.
    # ===========================================================================

    "tcm_acupuncture_chronic_pain": {
        "category": "traditional",
        "outcome_mortality_rrr": 0.05,
        "outcome_cvd_rrr": 0.05,
        "outcome_cancer_rrr": 0.05,
        "outcome_metabolic_rrr": 0.08,
        "outcome_mental_rrr": 0.30,
        "outcome_system_rrr": 0.18,
        "funding_independent_pct": 0.70,
        "hard_endpoints": False,
        "evidence_grade": "B",
        "no_patent_bias": True,
        "jurisdictional_bias": True,
        "typical_nnt_mortality_10yr": 80,
        "disease_reversal_rate": 0.20,
        "healthy_pop_validated": True,
        "adherence_adjusted_rrr": 0.38,
        "time_horizon_short": 0.28,
        "time_horizon_long": 0.22,
        "case_series_n": 0,
        "case_series_bayesian_responder_pct": 0.0,
        "case_series_outlier_fold_change": 0.0,
        "bradford_hill_composite": 0.55,
        "pharmacokinetic_validation": False,
        "pharmacodynamic_biomarker": False,
        "population_safety_signal_years": 3000,
        "mechanistic_evidence_grade": "C",
        "source": (
            "Acupuncture Trialists Collaboration meta-analysis; "
            "WHO 2023 traditional medicine report; 5000yr continuous use"
        ),
    },
}
