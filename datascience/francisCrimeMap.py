import pandas as pd
import numpy as np

df_crimes = pd.read_csv('crimes_2016.csv')
results = df_crimes['PdDistrict'].value_counts()
df_results = pd.DataFrame(results)
df_results.reset_index(inplace=True)
df_results.rename(columns={'index': 'Neighborhood', 'PdDistrict': 'Count'}, inplace=True)

!conda install -c conda-forge folium=0.5.0 --yes
import folium

threshold_scale = np.linspace(df_results['Count'].min(),
                              df_results['Count'].max(),
                              6, dtype=int)
threshold_scale = threshold_scale.tolist() # change the numpy array to a list
threshold_scale[-1] = threshold_scale[-1] + 1
francis_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)
francis_map.choropleth(
    geo_data='san-francisco.json',
    data=df_results,
    columns=['Neighborhood','Count'],
    threshold_scale=threshold_scale,
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Fransisco'
)
francis_map