import os
import pandas as pd

agg_file = 'medbr/data/plancoverage/transformed/plancoverage.csv'

df = pd.read_csv(f'medbr/data/plancoverage/raw/data.csv', sep=';')

df = df[['CD_MUNICIPIO', 'CD_OPERADORA', 'ID_PLANO']].groupby(['CD_MUNICIPIO', 'CD_OPERADORA']).count().reset_index()

df = df.rename(columns={
    "CD_MUNICIPIO": "city_code",
    "CD_OPERADORA": "operator",
    "ID_PLANO": "count"
})

df.to_csv(agg_file, index=False, sep=';')