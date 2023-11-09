import os
import pandas as pd

agg_file = 'medbr/data/birth/transformed/birth.csv'

for year in ['2021', '2022']:
    
    df = pd.read_csv(f'medbr/data/birth/raw/data_{year}.csv', sep=';', dtype={'DTNASC': str})
    
    df['DTNASC'] = pd.to_datetime(df['DTNASC'], format='%d%m%Y')
    df = df[['CODMUNNASC', 'DTNASC', 'HORANASC']].groupby(['CODMUNNASC', 'DTNASC']).count().reset_index()

    df = df.rename(columns={
        "CODMUNNASC": "city_code",
        "DTNASC": "birth_date",
        "HORANASC": "birth_count"
    })

    if os.path.exists(agg_file):
        df.to_csv(agg_file, index=False, sep=';', mode='a', header=False)
    else:
        df.to_csv(agg_file, index=False, sep=';')