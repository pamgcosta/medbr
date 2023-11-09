import os
import pandas as pd

agg_file = 'medbr/transformed/mortality.csv'

for year in ['2021', '2022']:
    
    df = pd.read_csv(f'medbr/data/mortality/raw/data_{year}.csv', sep=';', dtype={'DTOBITO': str})
    
    df['DTOBITO'] = pd.to_datetime(df['DTOBITO'], format='%d%m%Y')
    df = df[['CODMUNOCOR', 'DTOBITO', 'HORAOBITO']].groupby(['CODMUNOCOR', 'DTOBITO']).count().reset_index()

    df = df.rename(columns={
        "CODMUNOCOR": "city_code",
        "DTOBITO": "death_date",
        "HORAOBITO": "death_count"
    })

    if os.path.exists(agg_file):
        df.to_csv(agg_file, index=False, sep=';', mode='a', header=False)
    else:
        df.to_csv(agg_file, index=False, sep=';')