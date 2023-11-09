from urllib.error import HTTPError
import requests
import folium
import pandas as pd

def uri_request(uris, params, request_type='get', auth=None):
    """Request a uri and return a file-like object."""

    for uri in uris:
        uri = uri_creator(uri, params)
        
        try:
            if request_type == 'get':
                response = requests.get(uri)
            else:
                response = requests.post(uri, data=params, auth=auth)

            if response.status_code == 200:
                return response.content
        except HTTPError:
            raise ValueError("Invalid URL")


def uri_creator(uri, params: dict):
    
    params = "&".join([f"{k}={v}" for k, v in params.items()])

    return f'{uri}?{params}'


def remove_nil(data: dict):
    """Remove nil values from dict."""

    return {k: v for k, v in data.items() if v is not None}


def map_create(data, endpoint, city_name=None, city_code=None, location=None, **kwargs):
    
    if city_name is not None and city_code is not None:
        city = get_city(city_name=city_name, city_code=city_code)
        centroid = city['geometry'].iloc[0].centroid
        location = [centroid.y, centroid.x]
        
        m = folium.Map(location, **kwargs)   
        folium.GeoJson(city['geometry']).add_to(m)

    else:
        m = folium.Map(location, **kwargs)

    for i in data:
        folium.Marker([i[endpoint['lat']], i[endpoint['long']]], popup=i[endpoint['name']]).add_to(m)
    
    return m

def get_city(city_name=None, city_code=None):
    import geopandas as gpd

    cities = gpd.read_file('medbr/data/cities/transformed/cities.shp')
    if city_name is not None:
        city = cities[cities['city_name'].isin(city_name)]
    elif city_code is not None:
        city = cities[cities['city_code'].isin(city_code)]
    else:
        return cities # return all mo
    
    del cities
    return city


def colormap_create(data):
    from branca.colormap import linear

    br_estados = 'medbr/data/cities/raw/br_states.json'
    geo_json_data = json.load(open(br_estados))

    cities = gpd.read_file('medbr/data/cities/transformed/cities.shp')
    cities = cities.set_index('city_code')

    colormap = linear.YlOrRd_09.scale(data.min(), data.max())

    m = folium.Map(location=[48,-102],
                tiles='cartodbpositron',#'cartodbpositron', stamentoner
                zoom_start=3,
                control_scale=True)

    folium.GeoJson(
        cities.to_json(),
        name='count',
        style_function=lambda feature: {
            'fillColor': colormap(data[feature['city_code']]),
            'color': 'black',
            'weight': 0.3,
    }).add_to(m)

    return m