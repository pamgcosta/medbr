import os
import geopandas as gpd

agg_file = 'medbr/data/cities/transformed/cities.shp'

df = gpd.read_file('medbr/data/cities/raw/BR_Municipios_2022.shp')

df['CD_MUN_CO'] = df.CD_MUN.str[:-1]

df = df[['CD_MUN_CO', 'geometry', 'CD_MUN', 'NM_MUN']].groupby(['CD_MUN_CO', 'geometry', 'NM_MUN']).count().reset_index()

df = df[['CD_MUN_CO', 'geometry', 'NM_MUN']]

df = df.rename(columns={
    "CD_MUN_CO": "city_code",
    "NM_MUN": "city_name"
})

df.to_file(agg_file, driver='ESRI Shapefile')