import os
import pandas as pd

agg_file = 'medbr/data/beneficiaries/transformed/beneficiaries.csv'

df = pd.concat([
    pd.read_csv('medbr/data/beneficiaries/raw/tb_br_2209.csv', sep=';'),
    pd.read_csv('medbr/data/beneficiaries/raw/tb_br_2212.csv', sep=';'),
    pd.read_csv('medbr/data/beneficiaries/raw/tb_br_2303.csv', sep=';'),
    pd.read_csv('medbr/data/beneficiaries/raw/tb_br_2306.csv', sep=';')
])

df = df[['SG_UF', 'NR_BENEF_T']].groupby(['SG_UF']).sum('NR_BENEF_T').reset_index()

df = df.rename(columns={
    "SG_UF": "uf",
    "NR_BENEF_T": "beneficiaries_count"
})

df.to_csv(agg_file, index=False, sep=';')