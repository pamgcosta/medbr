import pandas as pd

from medbr.utils import colormap_create_uf

DATAPATH = 'medbr/data/beneficiaries/transformed/beneficiaries.csv'

def beneficiaries():
    
    data = pd.read_csv(DATAPATH, sep=';')

    data = data.set_index('uf')['beneficiaries_count']

    return colormap_create_uf(data)

