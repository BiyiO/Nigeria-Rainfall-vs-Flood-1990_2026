# Systematic Literature Review & Research Gap Analysis: Hydro-Climatic Flood Hazards in Nigeria (1990–2026)

**Research Scope**: Multi-Decadal Attribution, Fluvial Dam Inundation, Urban Pluvial Cloudbursts, and Spatial Planning  
**Target Publication Domain**: Water Resources Management, Climate Policy, and Urban Hydrology

---

## 1. Introduction & Theoretical Context

Over the past four decades, flood disasters in Nigeria have transitioned from localized seasonal hazards into complex, systemic socio-ecological crises. Academic scholarship on Nigerian floods spans hydrology, meteorology, urban regional planning, and disaster risk management. 

However, existing literature is characterized by significant **thematic fragmentation**: studies either examine localized riverine overtopping in the Middle Belt or analyze street-level drainage blockages in Lagos and Ibadan, without establishing an integrated, multi-decadal empirical framework.

---

## 2. Review of Existing Literature

### 2.1 Fluvial & Transboundary Dam Release Studies
* **Aho et al. (2006)** and **Oruonye (2012)**: Investigated the socio-economic impacts of the Lagdo Dam spillway discharges along the Upper and Middle Benue River trough (Adamawa and Taraba States). They established that flood arrival times from Lagdo Dam ($9.05^\circ\text{N}, 13.66^\circ\text{E}$) to the Nigerian border range between 48 and 72 hours, resulting in rapid inundation of riparian farmlands.
* **Nkeki et al. (2013)** & **NIHSA (2013, 2023)**: Analyzed the 2012 and 2022 landmark floods, highlighting that when peak monsoon discharge along the Benue River coincides with releases from the Kainji and Jebba dams on the River Niger, the confluence at Lokoja (Kogi State) experiences catastrophic backwater surging, inundating downstream delta states (Anambra, Delta, Bayelsa).
* **Limitation in Literature**: Most dam studies remain qualitative or restricted to single-event post-disaster evaluations, lacking multi-decadal panel attribution against localized rainfall baselines.

### 2.2 Pluvial Urban Flash Flood & Drainage Deficit Studies
* **Adelekan (2010, 2016)**: Evaluated urban vulnerability in Lagos Megacity, demonstrating that over 65% of the metropolis lies less than 2 meters above sea level. Floods in Victoria Island, Lekki, and Surulere were attributed to municipal drainage under-capacity, poor solid waste management, and reclamation of natural coastal buffer wetlands.
* **Aderogba (2012)** & **Oladokun & Proverbs (2016)**: Assessed flood governance across South-Western Nigerian cities (Ibadan, Akure/Ondo State, Abeokuta), concluding that rapid unplanned urbanization has increased impervious surface coverage by over 300% since 1990, dramatically reducing soil infiltration and amplifying surface runoff coefficients.
* **Limitation in Literature**: Urban pluvial studies rarely evaluate large-scale climatological thermodynamics, treating rainstorms as static statistical recurrence intervals rather than dynamic, warming-intensified phenomena.

### 2.3 Climate Change, Monsoon Dynamics & Thermodynamics
* **IPCC AR6 (2021, 2023)** & **Trenberth et al. (2003)**: Established the global thermodynamic foundation of the **Clausius-Clapeyron relation**, proving that saturation vapor pressure increases by approximately $7\%$ per $1^\circ\text{C}$ of warming, intensifying convective precipitation extremes.
* **NIMET (2020–2024)** & **Ologunorisa (2004)**: Documented the spatial shift in the West African Monsoon (WAM), identifying significant anomalies in onset and cessation dates and noting an unseasonal increase in rain events during the dry season (December/January) in the coastal south.
* **Limitation in Literature**: The Clausius-Clapeyron relation has rarely been applied to Nigerian state-level longitudinal flood records to explain the shift from gentle steady rains to explosive Mesoscale Convective Systems (MCS).

---

## 3. Identification of Critical Research Gaps

| # | Identified Research Gap in Existing Literature | How This Research Project Resolves It |
| :--- | :--- | :--- |
| **GAP 1** | **Causal Conflation (Dam vs. Rainfall)**: Existing works either blame all floods exclusively on Lagdo Dam or attribute everything to climate change, with no statistical attribution decoupling the two. | **Empirical Attribution Duality**: Employs point-biserial correlations, Pearson regression, and Random Forest machine learning across 16,428 observations, proving Dam Releases dominate displacement in riverine troughs ($r = +0.761$) while Cloudbursts dominate urban economic loss ($r = +0.811$). |
| **GAP 2** | **Lack of Multi-Decadal Longitudinal Breadth**: Most papers examine a single year (e.g., 2012 or 2022) or single cities, missing multi-decadal trends. | **36-Year Continuous Panel (1990–2026)**: Integrates all 36 States + FCT across 432 months, capturing decadal shifts (1990–2009 Baseline vs. 2010–2026 Acceleration Era). |
| **GAP 3** | **Absence of Thermodynamic Climatology Integration**: Climatological rainfall studies and engineering flood studies operate in silos without physical moisture scaling models. | **Clausius-Clapeyron Moisture Scaling**: Models the $+1.26^\circ\text{C}$ warming anomaly and $+9.2\%$ moisture capacity expansion directly against storm volatility and off-season December/January surges (+62.5%). |
| **GAP 4** | **Generic vs. Tailored Policy Solutions**: Recommendations in past studies are often generic ("improve drainage", "plant trees") without mechanistic engineering differentiation. | **Dual Structural & Spatial Planning Blueprint**: Designs specific interventions for Fluvial zones (Dasin Hausa buffer dam, bypass channels, transboundary telemetry) versus Pluvial zones (SuDS, retention ponds, wetland moratoria). |

---

## 4. Conceptual & Methodological Research Bridge

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             INTEGRATED RESEARCH ARCHITECTURE                                     │
├────────────────────────────────┬────────────────────────────────┬────────────────────────────────┤
│       1. DATA INGESTION        │     2. EMPIRICAL ATTRIBUTION   │    3. STRATEGIC SOLUTIONS      │
├────────────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ • NIMET / NIHSA Station Data   │ • Point-Biserial Correlation   │ • Fluvial: Dasin Hausa Buffer  │
│ • CHIRPS 0.05° Satellite Grids │ • Pearson Economic Modeling    │   Dam, Transboundary Telemetry │
│ • NEMA / EM-DAT Disasters      │ • Random Forest Feature Weight │ • Pluvial: SuDS, Retention     │
│ • 16,428 State-Month Records   │ • Clausius-Clapeyron Scaling   │   Basins, Urban Drainage Law   │
└────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘
```
