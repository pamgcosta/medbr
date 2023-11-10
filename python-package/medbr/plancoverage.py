import pandas as pd

from medbr.utils import colormap_create

DATAPATH = 'medbr/data/plancoverage/transformed/plancoverage.csv'

def plancoverage(ufs, operators=None):
    
    data = pd.read_csv(DATAPATH, sep=';')

    # cities = get_cities(ufs=ufs)
    # data = pd.merge(data, cities, how='inner', on='city_code')

    if operators is not None:
        data = data[data['operators'].isin(operators)]
    
    data.city_code = data.city_code.astype(str)
    data = data[['city_code', 'count']]

    data = data.groupby('city_code').sum('count').reset_index()
    data = data.set_index('city_code')['count']

    return colormap_create(data, ufs=ufs)

