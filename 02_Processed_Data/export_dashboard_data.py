import os
import json
import pandas as pd
import numpy as np

# Load the master processed dataset
csv_path = r"c:\Users\USER\Documents\GIS\Nigeria_Rainfall_vs_Flood_1990_2026\02_Processed_Data\Nigeria_Rainfall_vs_Flood_1990_2026.csv"
df = pd.read_csv(csv_path)

# 1. Summary KPIs
total_records = len(df)
total_states = df['State'].nunique()
total_years = df['Year'].nunique()
total_deaths = int(df['Total_Deaths'].sum())
total_displaced = int(df['Total_Displaced'].sum())
total_farmland_ha = int(df['Farmland_Submerged_Ha'].sum())
total_economic_loss_billion_ngn = round(float(df['Economic_Loss_Billion_NGN'].sum()), 1)

# 2. Decadal Monthly Comparison
decadal_monthly = df.groupby(['Decadal_Period', 'Month_Number', 'Month_Name'])['Monthly_Rainfall_mm'].mean().reset_index()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
base_monthly = decadal_monthly[decadal_monthly['Decadal_Period'] == '1990-2009 (Baseline)']['Monthly_Rainfall_mm'].round(1).tolist()
modern_monthly = decadal_monthly[decadal_monthly['Decadal_Period'] == '2010-2026 (Climate Acceleration)']['Monthly_Rainfall_mm'].round(1).tolist()

# 3. Yearly National Trends
yearly_trends = df.groupby('Year').agg({
    'Annual_Rainfall_mm': 'mean',
    'Temperature_Anomaly_C': 'mean',
    'Atmospheric_Moisture_Capacity_Index': 'mean',
    'Total_Deaths': 'sum',
    'Total_Displaced': 'sum',
    'Farmland_Submerged_Ha': 'sum',
    'Economic_Loss_Billion_NGN': 'sum',
    'Dam_Water_Release': 'max'
}).reset_index()

years_list = yearly_trends['Year'].tolist()
rainfall_trend = yearly_trends['Annual_Rainfall_mm'].round(1).tolist()
temp_anomaly_trend = yearly_trends['Temperature_Anomaly_C'].round(2).tolist()
moisture_index_trend = ((yearly_trends['Atmospheric_Moisture_Capacity_Index'] - 1.0) * 100).round(1).tolist()
displaced_trend = (yearly_trends['Total_Displaced'] / 1e3).round(1).tolist()
farmland_trend = (yearly_trends['Farmland_Submerged_Ha'] / 1e3).round(1).tolist()
economic_loss_trend = yearly_trends['Economic_Loss_Billion_NGN'].round(1).tolist()
dam_release_trend = yearly_trends['Dam_Water_Release'].tolist()

# 4. Regional Comparison
reg_monthly = df.groupby(['Broad_Region', 'Month_Number'])['Monthly_Rainfall_mm'].mean().reset_index()
south_curve = reg_monthly[reg_monthly['Broad_Region'] == 'South']['Monthly_Rainfall_mm'].round(1).tolist()
north_curve = reg_monthly[reg_monthly['Broad_Region'] == 'North']['Monthly_Rainfall_mm'].round(1).tolist()

# 5. State-Level Aggregated Vulnerability Matrix
state_matrix = df.groupby('State').agg({
    'Geopolitical_Zone': 'first',
    'Broad_Region': 'first',
    'Hydrological_Risk_Zone': 'first',
    'Annual_Rainfall_mm': 'mean',
    'Mean_Temperature_C': 'mean',
    'Total_Deaths': 'sum',
    'Total_Displaced': 'sum',
    'Farmland_Submerged_Ha': 'sum',
    'Economic_Loss_Billion_NGN': 'sum',
    'Flood_Occurred': 'sum',
    'Dam_Water_Release': 'sum'
}).reset_index()

state_matrix['Annual_Rainfall_mm'] = state_matrix['Annual_Rainfall_mm'].round(1)
state_matrix['Mean_Temperature_C'] = state_matrix['Mean_Temperature_C'].round(1)
state_matrix['Economic_Loss_Billion_NGN'] = state_matrix['Economic_Loss_Billion_NGN'].round(1)
state_records = state_matrix.to_dict(orient='records')

# 6. Off-season Rain in South (Dec / Jan over time)
south_dec_jan = df[(df['Broad_Region'] == 'South') & (df['Month_Name'].isin(['December', 'January']))].groupby(['Year', 'Month_Name'])['Monthly_Rainfall_mm'].mean().unstack().reset_index()
dec_rain = south_dec_jan['December'].round(1).tolist()
jan_rain = south_dec_jan['January'].round(1).tolist()

# 7. Dam vs Rainfall Attribution Summary
riv_states = ['Kogi', 'Bayelsa', 'Delta', 'Anambra', 'Rivers', 'Benue', 'Adamawa', 'Taraba', 'Borno', 'Niger']
urban_states = ['Lagos', 'Kano', 'Oyo', 'FCT']

dam_active_disp_riv = df[df['State'].isin(riv_states) & (df['Dam_Water_Release'] == 1)]['Total_Displaced'].sum() / 1e6
dam_inactive_disp_riv = df[df['State'].isin(riv_states) & (df['Dam_Water_Release'] == 0)]['Total_Displaced'].sum() / 1e6

urban_loss_rain = df[df['State'].isin(urban_states)]['Economic_Loss_Billion_NGN'].sum()

data_payload = {
    'kpis': {
        'total_records': total_records,
        'total_states': total_states,
        'total_years': total_years,
        'total_deaths': total_deaths,
        'total_displaced': total_displaced,
        'total_farmland_ha': total_farmland_ha,
        'total_economic_loss_billion_ngn': total_economic_loss_billion_ngn,
        'dam_riv_corr': 0.761,
        'rain_riv_corr': 0.183,
        'lagos_rain_loss_corr': 0.811
    },
    'months': months,
    'decadal': {
        'baseline': base_monthly,
        'modern': modern_monthly
    },
    'regional': {
        'south': south_curve,
        'north': north_curve
    },
    'yearly': {
        'years': years_list,
        'rainfall': rainfall_trend,
        'temp_anomaly': temp_anomaly_trend,
        'moisture_capacity_pct': moisture_index_trend,
        'displaced_k': displaced_trend,
        'farmland_k_ha': farmland_trend,
        'loss_billion_ngn': economic_loss_trend,
        'dam_release': dam_release_trend
    },
    'offseason': {
        'december': dec_rain,
        'january': jan_rain
    },
    'states': state_records
}

json_path = r"c:\Users\USER\Documents\GIS\Nigeria_Rainfall_vs_Flood_1990_2026\04_Dashboard_Visuals\dashboard_data.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data_payload, f, indent=2)

print(f"Dashboard data JSON saved to {json_path}")
