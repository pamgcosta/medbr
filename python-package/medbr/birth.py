import geopandas as gpd
import folium
import webbrowser
import pandas as pd
import json
import functools 
import numpy as np


from medbr.utils import remove_nil, get_cities
from folium.plugins import HeatMapWithTime

DATAPATH = 'medbr/data/birth/transformed/birth.csv'

def birth(cities_code=None, start_at=None, end_at=None):
    
    data = pd.read_csv(DATAPATH, sep=';')
    
    if cities_code is not None:
        data = data[data['city_code'].isin(cities_code)]
    
    data = data[(data['birth_date'] >= start_at) & (data['birth_date'] <= end_at)]

    if len(data) == 0:
        raise ValueError("No data found.")


    cities = get_cities(city_code=cities_code)
    data = pd.merge(data, cities, how='inner', on='city_code')

    time_index = list(data['birth_date'].sort_values().astype('str').unique())

    data['birth_date'] = data['birth_date'].sort_values(ascending=True)
    arr = []
    for _, d in data.groupby('birth_date'):
        arr.append([[row['geometry'].centroid.y, row['geometry'].centroid.x, row['birth_count']] for _, row in d.iterrows()])
    
    return heatmap_create(time_index, arr)

def heatmap_create(time_index, data):
    
    hmt = folium.Map(location=[data[0][0][0], data[0][0][1]],
                tiles='cartodbpositron',#'cartodbpositron', stamentoner
                zoom_start=3,
                control_scale=True)

    HeatMapWithTime(data,
                    index=time_index,
                    auto_play=False,
                    use_local_extrema=True
                ).add_to(hmt)

    return hmt