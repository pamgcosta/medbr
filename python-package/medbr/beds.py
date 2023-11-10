import pandas as pd

from medbr.utils import colormap_create_uf

DATAPATH = 'medbr/data/beds/transformed/beds.csv'

def beds():
    
    data = pd.read_csv(DATAPATH, sep=';')

    data = data.set_index('uf')['beds_count']

    return colormap_create_uf(data)

