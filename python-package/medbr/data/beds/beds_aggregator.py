import os
import pandas as pd

agg_file = 'medbr/data/beds/transformed/beds.csv'

df = pd.read_csv(f'medbr/data/beds/raw/data_2023.csv', encoding='latin-1')

df = df[['UF', 'LEITOS_EXISTENTES']].groupby(['UF']).sum('LEITOS_EXISTENTES').reset_index()

df = df.rename(columns={
    "UF": "uf",
    "LEITOS_EXISTENTES": "beds_count"
})

df.to_csv(agg_file, index=False, sep=';')