import os
import pandas as pd

agg_file = 'medbr/data/beds/transformed/beds.csv'

for year in ['2023']:
    
    df = pd.read_csv(f'medbr/data/beds/raw/data_{year}.csv', encoding='latin-1')
    
    df['DTNASC'] = pd.to_datetime(df['DTNASC'], format='%d%m%Y')
    df = df[['CODMUNNASC', 'DTNASC', 'HORANASC']].groupby(['CODMUNNASC', 'DTNASC']).count().reset_index()

    df = df.rename(columns={
        "CODMUNNASC": "city_code",
        "DTNASC": "beds_date",
        "HORANASC": "beds_count"
    })

    if os.path.exists(agg_file):
        df.to_csv(agg_file, index=False, sep=';', mode='a', header=False)
    else:
        df.to_csv(agg_file, index=False, sep=';')