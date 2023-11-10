import os
import geopandas as gpd

agg_file = 'medbr/data/cities/transformed/cities.shp'

df = gpd.read_file('medbr/data/cities/raw/BR_Municipios_2022.shp')

df['CD_MUN_CO'] = df.CD_MUN.str[:-1]

df = df[['CD_MUN_CO', 'geometry', 'NM_MUN', 'SIGLA_UF']]

df = df.rename(columns={
    "CD_MUN_CO": "city_code",
    "NM_MUN": "city_name",
    "SIGLA_UF": "uf"
})

df['city_code'] = df['city_code'].astype('int64')

df.to_file(agg_file, driver='ESRI Shapefile')