import pandas as pd
import matplotlib.pyplot as plt

#1. Anaise de cescimento Populacional e Consumo de Energia
df_brazil_eua = pd.read_csv('dados_brazil_eua.csv')
df_grouped = df_brazil_eua.groupby(['year', 'country']).agg({
    'population' : 'sum',
    'wind_electricity' : 'sum',
    'hydro_electricity' : 'sum',
    'nuclear_electricity' : 'sum'
    }).reset_index()

df_grouped['decade'] = (df_grouped['year'] // 10 ) * 10

# criand grfc p tds fontes de energia
plt.figure(figsize=(30, 20))

# largura das barras
bar_width = 1.2

colors_br = {
 'wind_electricity' : 'green',
    'hydro_electricity' : 'blue',
    'nuclear_electricity' : 'purple'   
}

colors_eua ={
    'wind_electricity' : 'grey',
    'hydro_electricity' : 'cyan',
    'nuclear_electricity' : 'red'
}
for idx, country in enumerate(df_grouped['country'].unique()):
    df_country = df_grouped[df_grouped['country'] == country]
    
    # posição das barras para cada tipo de energia
    positions = df_country['decade'] + idx * bar_width  

    if country == 'Brazil':
        plt.bar(positions - bar_width, df_country['wind_electricity'], width=bar_width, label=f'{country} - Eólica', color = colors_br['wind_electricity'])
        plt.bar(positions, df_country['hydro_electricity'], width=bar_width, label=f'{country} - Hidrolétrica', color = colors_br['hydro_electricity'])
        plt.bar(positions + bar_width, df_country['nuclear_electricity'], width=bar_width, label=f'{country} - Nuclear', color = colors_br['nuclear_electricity'])
    elif country == 'United States':
        plt.bar(positions - bar_width, df_country['wind_electricity'], width=bar_width, label=f'{country} - Eólica', color = colors_eua['wind_electricity'])
        plt.bar(positions, df_country['hydro_electricity'], width=bar_width, label=f'{country} - Hidrolétrica', color = colors_eua['hydro_electricity'])
        plt.bar(positions + bar_width, df_country['nuclear_electricity'], width=bar_width, label=f'{country} - Nuclear', color = colors_eua['nuclear_electricity'])
        
    
#grafico    
plt.title('Comparação de Fontes de Energia ao Longo das Décadas')
plt.xlabel('Década')
plt.ylabel('Produção de Energia (em GWh)')
plt.legend()
plt.grid(True, axis='y')
plt.xticks(df_grouped['decade'].unique())
plt.show()


#2. Participação de Cada Fonte de Energia na Geração Total
#3. Comparação Entre Brasil e EUA no Uso de Fontes Renováveis vs. Não Renováveis
#4. Análise de Tendência no Crescimento da Energia Eólica
#5. Correlação entre População e Consumo de Energia
#7. Análise de Outliers nas Fontes de Energia
#8. Impacto da Energia Hidrelétrica no Brasil