import pandas as pd 

df = pd.read_csv('owid-energy-data.csv')

df_brazil_eua = df[(df['country'] == 'Brazil') | (df['country'] == 'United States')]
df_brazil_eua = df_brazil_eua[['country', 'year', 'population', 'wind_electricity', 'hydro_electricity', 'nuclear_electricity']]

df_brazil_eua.to_csv('dados_brazil_eua.csv', index=False)



