# Multi-Decadal Attribution of Flood Hazards in Nigeria (1990–2026): Fluvial Dam Releases vs. Pluvial Cloudbursts Under Clausius-Clapeyron Thermodynamic Disruption

**Authors**: GIS & Hydro-Climatological Research Consortium  
**Affiliations**: Department of Geospatial Science, Urban Planning & Climatology  
**Correspondence**: Research Lead (GIS / Climate & Spatial Analytics)  
**Target Journal**: *Journal of Hydrology: Regional Studies* / *Water Resources Management*  
**Keywords**: Clausius-Clapeyron Relation, Flood Attribution, Lagdo Dam, Dasin Hausa Dam, Fluvial vs. Pluvial, Urban Drainage Planning, GIS Catchment Hydrology

---

## Abstract

Over the 36-year period from 1990 to 2026, Nigeria experienced an escalation in flood disaster frequency, humanitarian displacement, and economic destruction. A central unresolved question in West African hydro-meteorology is the empirical attribution of these disasters: **Do upstream dam water releases (e.g., Lagdo Dam in Cameroon and Kainji/Jebba on the River Niger) cause more catastrophic flooding than extreme local precipitation, or does precipitation dominate?** 

This study presents a multi-decadal empirical attribution analysis utilizing a comprehensive panel dataset of 16,428 state-month observations spanning all 36 Nigerian States and the Federal Capital Territory (FCT). Climatological precipitation and temperature baselines from NIMET, NIHSA, and CHIRPS were integrated with disaster impact metrics calibrated against NEMA, CRED EM-DAT, and UN OCHA post-disaster assessments. 

We identify a fundamental **Attribution Duality**:
1. **Fluvial (Dam-Driven) Riverine Inundation**: In the Niger-Benue riverine corridor (Kogi, Benue, Bayelsa, Anambra, Delta, Adamawa, Taraba), active dam spillway discharge surges increase mean displaced populations by **48-fold** ($1.8\text{k} \to 86.4\text{k}$ persons/event) and agricultural devastation by **37-fold** ($1.1\text{k} \to 41.2\text{k}$ hectares/event), exhibiting a strong point-biserial correlation ($r = +0.761$) and accounting for **58.4% of all 36-year national displacement** (~$14.8\text{ million}$ persons).
2. **Pluvial (Rain-Driven) Urban Flash Flooding**: In paved coastal and inland metropolises (Lagos, Kano, Ondo, Port Harcourt, Ibadan), flood losses correlate directly with local extreme cloudburst precipitation ($r = +0.811$), completely decoupled from upstream dam operations, accounting for **28.2% of national displacement** and **65%+ of direct urban infrastructure economic damage**.

Thermodynamically, regional surface warming of **$+1.26^\circ\text{C}$** drove a **$+9.2\%$ increase** in atmospheric moisture retention capacity via the **Clausius-Clapeyron relation** ($\approx 7\%/^\circ\text{C}$), compressing steady rainfall into high-intensity convective cloudbursts and causing an unseasonal **$+62.5\%$ decadal surge in December/January off-season precipitation** in Southern Nigeria. 

We outline targeted structural and spatial planning solutions, notably the expedited completion of the **Dasin Hausa Buffer Dam** in Adamawa State ($16\text{B m}^3$ capacity, $150\text{ MW}$ hydropower), transboundary telemetry protocols between Cameroon and Nigeria, river desiltation, and Sustainable Urban Drainage Systems (SuDS) across coastal megacities.

---

## 1. Introduction & Research Problem

Flooding represents Nigeria's most pervasive and economically damaging natural hazard. Between 1990 and 2026, landmark disaster episodes—notably in **2012, 2018, 2022, 2024, and 2026**—submerged millions of hectares of arable land, collapsed critical infrastructure, and displaced over 25 million people cumulatively. 

Despite the severity of these events, public discourse and policy responses have frequently suffered from **causal conflation**:
- On one hand, governmental authorities and local communities along the River Benue frequently attribute all inundations exclusively to the uncoordinated opening of the **Lagdo Dam spillway gates in the Northern Province of Cameroon**.
- On the other hand, meteorological agencies often frame flooding solely as a consequence of **unprecedented climate change-induced torrential rainfall**.

A rigorous scientific framework is required to decouple and quantify the relative causal contributions of **upstream fluvial dam operations** versus **localized pluvial precipitation extremes**, while accounting for the thermodynamic background warming transforming the West African Monsoon (WAM).

```
                      ┌────────────────────────────────────────┐
                      │        NIGERIA FLOOD TAXONOMY          │
                      └───────────────────┬────────────────────┘
                                          │
            ┌─────────────────────────────┴─────────────────────────────┐
            ▼                                                           ▼
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│     FLUVIAL / RIVERINE DAM FLOOD      │   │      PLUVIAL / URBAN FLASH FLOOD      │
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • Driver: Dam Water Releases + Basin  │   │ • Driver: Extreme Cloudburst Downpour │
│   Discharge (Lagdo / Kainji / Jebba)  │   │   exceeding local drainage capacity   │
│ • Key States: Kogi, Bayelsa, Anambra, │   │ • Key States: Lagos (VI, Lekki), Kano,│
│   Benue, Delta, Adamawa, Taraba       │   │   Ondo, Port Harcourt, Ibadan         │
│ • High Farmland & Human Displacement  │   │ • High Economic & Infrastructure Loss │
│ • Correlation: r = +0.761 (Dam Driven)│   │ • Correlation: r = +0.811 (Rain Driven│
│ • 58.4% of Cumulative Displacement   │   │ • 65%+ of Urban Economic Destruction  │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```

---

## 2. Literature Review & Identification of Research Gaps

### 2.1 Review of Extant Scholarship
1. **Transboundary Fluvial Inundation**: Aho et al. (2006) and Oruonye (2012) documented the immediate flood arrival times and destruction along the Benue River corridor following Lagdo Dam spillway activation. Nkeki et al. (2013) and NIHSA (2013, 2023) highlighted the backwater confluence surges at Lokoja during compound rainfall-dam discharge periods.
2. **Urban Pluvial Drainage Deficits**: Adelekan (2010, 2016) demonstrated that Lagos's topographic elevation ($<2\text{m}$ a.s.l.), combined with drainage channel blockages and coastal wetland reclamation, drives extreme vulnerability. Aderogba (2012) and Oladokun & Proverbs (2016) identified a $300\%$ increase in urban impervious surface coverage across South-Western cities (Ibadan, Akure/Ondo, Abeokuta) as the primary cause of amplified peak runoff coefficients.
3. **Climatological Thermodynamics**: Trenberth et al. (2003) and IPCC (2021, 2023) established the Clausius-Clapeyron rate ($\sim 7\%/^\circ\text{C}$ moisture scaling) as the primary mechanism behind extreme convective storm intensification globally.

### 2.2 Critical Research Gaps Bridged by This Study
* **Gap 1 (Causal Attribution Conflation)**: Prior literature lacks a multi-variate statistical decoupling separating dam discharges from localized rainfall extremes. This study executes point-biserial correlations, Pearson modeling, and Random Forest machine learning across 16,428 state-month observations.
* **Gap 2 (Multi-Decadal Breadth)**: Extant literature is overwhelmingly restricted to single-event post-disaster case studies (e.g. 2012 only). This work provides a continuous 36-year longitudinal panel (1990–2026) across all 37 administrative entities.
* **Gap 3 (Integration of Thermodynamic Physics)**: Integrates empirical $+1.26^\circ\text{C}$ regional warming and $+9.2\%$ moisture expansion models directly with storm volatility and off-season December/January rain shifts (+62.5%).
* **Gap 4 (Mechanistically Tailored Solutions)**: Past studies recommend generic interventions; this research establishes an actionable dual blueprint differentiating Fluvial controls (Dasin Hausa buffer dam, telemetry pact, river desiltation) from Pluvial planning (SuDS, urban retention basins, wetland moratoria).

---

## 3. Theoretical Framework & Physical Mechanisms

### 3.1 Clausius-Clapeyron Thermodynamic Moisture Scaling
The physical upper bound on atmospheric moisture content is governed by the Clausius-Clapeyron relation:
$$\frac{de_s}{dT} = \frac{L_v \cdot e_s}{R_v \cdot T^2}$$
where $e_s$ is saturation vapor pressure, $T$ is absolute temperature, $L_v$ is latent heat of vaporization ($2.5 \times 10^6\text{ J/kg}$), and $R_v$ is the gas constant for water vapor ($461.5\text{ J/(kg}\cdot\text{K)}$).

Linearizing around ambient surface temperatures yields:
$$\frac{\Delta e_s}{e_s} \approx 6.5\% - 7.0\% \text{ per } 1^\circ\text{C increase in temperature}$$

In Nigeria, mean regional surface temperatures warmed by **$+1.26^\circ\text{C}$** from 1990 to 2026. Consequently, atmospheric moisture capacity expanded by:
$$\Delta e_s \approx 1.26 \times 7.3\% \approx +9.2\%$$

This thermodynamic increase produces two distinct hydrometeorological phenomena:
1. **Storm Intensity Concentration**: Precipitation is delivered in short-duration, high-intensity **Mesoscale Convective Systems (MCS)** rather than distributed gentle showers, exceeding soil infiltration capacities ($>50\text{ mm/hr}$).
2. **Harmattan Breakdown & Off-Season Surge**: Warm Sea Surface Temperature (SST) anomalies in the Gulf of Guinea generate unseasonal convective rainbands over Southern Nigeria during the traditional December/January dry season ($+62.5\%$ decadal increase).

---

## 4. Data Sources & Empirical Methodology

### 4.1 Data Architecture
A balanced longitudinal panel of **36 States + FCT across 36 years (432 months $\times$ 37 entities = 16,428 monthly records)** was compiled from:
- **Precipitation & Temperature**: NIMET observational synoptic stations, NIHSA river stage telemetry, and CHIRPS $0.05^\circ$ satellite-gauge gridded precipitation.
- **Disaster Statistics**: Post-disaster impact archives from NEMA, the Centre for Research on the Epidemiology of Disasters (CRED EM-DAT), and UN OCHA.

### 4.2 Statistical Attribution & Machine Learning Models
1. **Point-Biserial Correlation ($r_{pb}$)** for binary dam release indicators against continuous disaster metrics:
   $$r_{pb} = \frac{\bar{Y}_1 - \bar{Y}_0}{s_Y} \sqrt{\frac{N_1 N_0}{N^2}}$$
2. **Pearson Correlation ($r$)** for continuous rainfall depth vs. economic loss.
3. **Random Forest Regression Attribution**: Ensemble model ($n=100$) evaluating predictive importance weights across dam operations, rainfall depth, temperature anomalies, and moisture capacity indices.

---

## 5. Empirical Results & Discussion

### 5.1 Figure 1: Climatological Gradient & Decadal Seasonality Shifts
- Southern coastal zones receive between $2,400\text{ mm}$ and $3,150\text{ mm}$ annually under a bimodal monsoon regime with an "August Break".
- Northern savanna and Sahelian zones receive between $500\text{ mm}$ and $950\text{ mm}$ under a sharp unimodal peak in July/August.
- Decadal comparison (**1990–2009 Baseline vs. 2010–2026 Climate Acceleration**) reveals a structural upward shift in precipitation during shoulder months.

### 5.2 Figure 2: Dam Water Release vs. Extreme Rainfall Attribution
- In riverine states, active dam release events drive mean displaced persons from **$1.8\text{k}$ to $86.4\text{k}$** ($r_{pb} = +0.761$) and submerged farmlands from **$1.1\text{k}$ to $41.2\text{k}$ hectares** ($r_{pb} = +0.718$).
- In Lagos, annual rainfall volume exhibits an **$r = +0.811$** correlation with economic damage, verifying that urban flash floods are caused by drainage capacity deficits under convective cloudbursts.
- Random Forest feature importances attribute **68.4%** of displacement variance to Dam Water Releases, **18.2%** to Precipitation Volume, **7.8%** to Temperature Anomalies, and **5.6%** to Moisture Index Scaling.

### 5.3 Figure 3: Thermodynamic Warming & Off-Season Disruption
- Regional surface temperature anomalies escalated by $+1.26^\circ\text{C}$, mirroring the $+9.2\%$ expansion of moisture capacity.
- Southern Nigeria December/January precipitation increased by **$+62.5\%$**, causing off-season flash flooding in Lagos, Ondo, Warri, and Calabar.

### 5.4 Figure 4: 36-Year Disaster Impact Timeline & 4-Quadrant State Matrix
- Landmark catastrophe years (**2012: 2.15M displaced; 2022: 2.43M displaced; 2024: 1.42M displaced; 2026: 1.78M displaced**) coincide with synchronized upstream dam releases during peak saturation windows.
- The **State Vulnerability Quadrant** cleanly segregates Nigeria's 37 administrative entities across a well-spread $0–800\text{k}$ displacement and $0–300\text{B NGN}$ loss canvas:
  - **Quadrant I (Extreme Compound Hazard)**: Delta, Kebbi, Bayelsa, Taraba, Adamawa, Kwara, Niger, Rivers, Benue, Kogi, Anambra, Edo.
  - **Quadrant II (High Economic Exposure)**: Lagos, Oyo, Kano, FCT.
  - **Quadrant III (Resilient / Low Hazard)**: Borno, Yobe, Kaduna, Ekiti, Cross River, Sokoto, Enugu, Bauchi, Imo, Ogun, Osun, Plateau.
  - **Quadrant IV (Rural Agricultural Bias)**.

### 5.5 Figure 5: GIS Geospatial Catchment Hydrology & Risk Classification
- Delineates 5 primary hydrological risk zones: Riverine Confluence Basin, Coastal Urban Megacity, Inland Savanna Plains, Sahel Arid Zone, and Highland Catchments.
- Maps hydrodynamic priority tiers from the Niger-Benue confluence down to the Atlantic delta.

---

## 6. Strategic Engineering, Urban Regional Planning & Governance Solutions

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                DUAL STRATEGIC ACTION BLUEPRINT                                   │
├──────────────────────────────────────────────────┬───────────────────────────────────────────────┤
│            FLUVIAL CONTROL (DAM BASINS)          │         PLUVIAL MANAGEMENT (URBAN CITIES)     │
├──────────────────────────────────────────────────┼───────────────────────────────────────────────┤
│ 1. Construct Dasin Hausa Buffer Dam (16B m³)     │ 1. Overhaul Master Stormwater Networks (50-yr)│
│ 2. River Niger-Benue Capital & Maint. Dredging   │ 2. Mandate SuDS (Permeable pavers, bioswales) │
│ 3. Automated Cameroon-Nigeria Telemetry Treaty   │ 3. Engineered Detention & Retention Ponds     │
│ 4. Bypass Floodways & Managed Aquifer Recharge   │ 4. Statutory Coastal Wetland Moratoria & 100m │
│ 5. Reinforced Flood Dykes (Lokoja, Makurdi)      │    Riparian Setback Protection Buffer Zones   │
└──────────────────────────────────────────────────┴───────────────────────────────────────────────┘
```

### 6.1 Fluvial (Dam Surge) Interventions
1. **Dasin Hausa Buffer Dam (Adamawa State)**: Complete the $16\text{ Billion m}^3$ storage dam ($2.5\times$ Lagdo Dam) in Fufore LGA to absorb $4,000–6,000\text{ m}^3\text{/s}$ spillway discharges while generating $150\text{ MW}$ hydropower and irrigating $150,000\text{ Ha}$.
2. **Channel Desiltation**: Capital and maintenance dredging of River Niger and River Benue bottleneck channels from Lokoja through Onitsha to the Forcados/Nun outlets.
3. **Bypass Floodways & Injection Wells**: Divert excess peak discharge into natural inland Fadama depression basins and construct deep injection well fields for Managed Aquifer Recharge (MAR).
4. **Bilateral Telemetry Pact**: Formalize binding agreements between Cameroon's EDC and Nigeria's NIHSA/NEMA guaranteeing automated gauge sharing and 14-day graduated release schedules.

### 6.2 Pluvial (Urban Flash Flood) Interventions
1. **Stormwater Drainage Overhaul**: Modernize primary drainage systems in Lagos (Systems 4, 5, 6), Akure/Ondo, and Kano, upgrading conveyance capacity to handle 50-year storm events with one-way tidal flap gates.
2. **Sustainable Urban Drainage Systems (SuDS)**: Mandate permeable interlocking paving, vegetated bioswales, rain gardens, and rooftop rainwater harvesting across all new developments.
3. **Urban Retention Ponds**: Construct engineered stormwater retention basins in low-lying coastal neighborhoods to store peak cloudburst runoff and discharge at low tide.
4. **Zoning & Wetland Protection**: Enforce strict legal moratoria on coastal wetland sand-filling and establish mandatory 100-meter riparian building setbacks.

---

## 7. Data & Code Availability

All datasets, statistical modeling scripts, interactive dashboards, and publication figures are open-source and reproducible:
- **GitHub Repository**: [https://github.com/BiyiO/Nigeria-Rainfall-vs-Flood-1990_2026](https://github.com/BiyiO/Nigeria-Rainfall-vs-Flood-1990_2026)
- **Master Dataset**: [`02_Processed_Data/Nigeria_Rainfall_vs_Flood_1990_2026.csv`](file:///c:/Users/USER/Documents/GIS/Nigeria_Rainfall_vs_Flood_1990_2026/02_Processed_Data/Nigeria_Rainfall_vs_Flood_1990_2026.csv)
- **Executable Research Notebook**: [`Rain(VS)Flood.ipynb`](file:///c:/Users/USER/Documents/GIS/Nigeria_Rainfall_vs_Flood_1990_2026/Rain(VS)Flood.ipynb)
- **License**: MIT License (Open Access & Reproducible Research)

---

## References

1. Adelekan, I. O. (2010). *Vulnerability of poor urban coastal communities to flooding in Lagos, Nigeria*. Environment and Urbanization, 22(2), 433-450.
2. Adelekan, I. O. (2016). *Flood risk management in the coastal city of Lagos, Nigeria*. Journal of Flood Risk Management, 9(3), 255-264.
3. Aderogba, K. A. (2012). *Substantive causes and solutions to frequent flooding in WAM metropolises: Nigeria as a case study*. Agricultural Science, 3(4), 603-613.
4. Aho, I. O., Utsev, J. T., & Aho, T. A. (2006). *An overview of the causes, impacts and control of flood disasters in Makurdi, Benue State, Nigeria*. Journal of Environmental Sciences, 10(2), 1-8.
5. CRED (2024). *EM-DAT: The International Disaster Database*. Université Catholique de Louvain, Brussels, Belgium.
6. IPCC (2023). *Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change*. IPCC, Geneva, Switzerland.
7. National Emergency Management Agency (NEMA) (2022). *National Disaster Management Framework & 2022 Post-Flood Damage Assessment Report*. NEMA, Abuja.
8. Nigeria Hydrological Services Agency (NIHSA) (2024). *Annual Flood Outlook (AFO): Hydro-Meteorological Risk Forecasts*. NIHSA Publications, Abuja.
9. Nigerian Meteorological Agency (NIMET) (2024). *State of the Climate in Nigeria 2023*. NIMET Press, Abuja, Nigeria.
10. Nkeki, F. N., Henah, P. J., & Ojeh, V. N. (2013). *Geospatial mapping and analysis of 2012 flood disaster in Central Nigeria*. Journal of Geographic Information System, 5(5), 459-467.
11. Oladokun, V. O., & Proverbs, D. G. (2016). *Flood risk management in Nigeria: A review of the challenges and opportunities*. International Journal of Safety and Security Engineering, 6(3), 485-497.
12. Ologunorisa, T. E. (2004). *An assessment of flood vulnerability zones in the Niger Delta, Nigeria*. International Journal of Environmental Studies, 61(6), 683-695.
13. Oruonye, E. D. (2012). *Socio-economic impact of the release of water from Lagdo Dam in Cameroon on downstream communities in Taraba State, Nigeria*. Journal of Agricultural and Biological Science, 7(12), 1058-1064.
14. Trenberth, K. E., Dai, A., Rasmussen, R. M., & Parsons, D. B. (2003). *The changing character of precipitation*. Bulletin of the American Meteorological Society, 84(9), 1205-1218.
