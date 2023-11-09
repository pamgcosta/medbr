import geopandas as gpd
import folium
import webbrowser
import pandas as pd
import json
import functools 
import numpy as np


from medbr.utils import uri_request, uri_creator, remove_nil, map_create

URI = ['https://imunizacao-es.saude.gov.br/_search']
AUTH = ('imunizacao_public', 'qlto5t&7r_@+#Tlstigi')

ENDPOINT_FIELDS = {
    "lat": "latitude_estabelecimento_decimo_grau",
    "long": "longitude_estabelecimento_decimo_grau",
    "name": "nome_razao_social"
}


def covid_vaccine(facility_type=None, state=None, 
                city=None, status=None, surgical_center=None, 
                obstetric_center=None, limit=None, offset=None):
    
    d = {
        "codigo_tipo_unidade": facility_type,
        "codigo_uf": state,
        "codigo_municipio": city,
        "status": status,
        "surgical_center": surgical_center,
        "obstetric_center": obstetric_center,
        "limit": limit,
        "offset": offset
    }

    d = remove_nil(d)

    data = uri_request(URI, d, request_type='post', auth=AUTH)
    data = json.loads(data.decode('utf-8'))

    data = data['estabelecimentos']

    if len(data) == 0:
        raise ValueError("No data found.")

    # lat_mean = np.mean([lat[ENDPOINT_FIELDS['lat']] for lat in data])
    # long_mean = np.mean([long[ENDPOINT_FIELDS['long']] for long in data])

    return map_create(
        data, 
        city,
        location=[lat_mean, long_mean], 
        endpoint=ENDPOINT_FIELDS,
        tiles='openstreetmap'
    )

