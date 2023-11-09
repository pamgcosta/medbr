import geopandas as gpd
import folium
import webbrowser
import pandas as pd
import json
import functools 
import numpy as np


from medbr.utils import remove_nil, get_city, colormap_create
from folium.plugins import HeatMapWithTime

DATAPATH = 'medbr/data/plancoverage/transformed/plancoverage.csv'

def plancoverage(cities_code=None, start_at=None, end_at=None):
    
    data = pd.read_csv(DATAPATH, sep=';')
    
    if cities_code is not None:
        data = data[data['city_code'].isin(cities_code)]

    if len(data) == 0:
        raise ValueError("No data found.")

    cities = get_city(city_code=cities_code)
    data = pd.merge(data, cities, how='inner', on='city_code')


    data
    data = data.groupby('id').sum('count')

    return colormap_create(data)

