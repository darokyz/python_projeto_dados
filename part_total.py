import pandas as pd

#2. Participação de Cada Fonte de Energia na Geração Total
df_brazil_eua = pd.read_csv('dados_brazil_eua.csv')
df_grouped = df_brazil_eua.groupby(['year', 'country']).agg({
    'wind_electricity': 'sum',
    'hydro_electricity': 'sum',
    'nuclear_electricity': 'sum',
}).reset_index()

df_grouped['total_generation'] = (
    df_grouped['wind_electricity'] + df_grouped['hydro_electricity'] + df_grouped ['nuclear_electricity']
)

df_grouped['wind_pct'] = (df_grouped['wind_electricity'] / df_grouped['total_generation']) * 100
df_grouped['hydro_pct'] = (df_grouped['hydro_electricity'] / df_grouped['total_generation']) * 100
df_grouped['nuclear_pct'] = (df_grouped['nuclear_electricity'] / df_grouped['total_generation']) * 100

for index, row in df_grouped.iterrows():
    print(f"\nAno: {int(row['year'])} | País: {row['country']}")
    print(f"  Eólica: {row['wind_pct']:.2f}%")
    print(f"  Hidro: {row['hydro_pct']:.2f}%")
    print(f"  Nuclear: {row['nuclear_pct']:.2f}%")