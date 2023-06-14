import requests
import json
import pandas as pd
from tqdm import tqdm

# Carregar o arquivo CSV 'movies.csv' em um DataFrame
df_movies = pd.read_csv('movies.csv', delimiter='|')

# Filtrar apenas os filmes de Ação/Aventura
df_filtered = df_movies[(df_movies['tempoMinutos'] != 'N') &
                        (df_movies['numeroVotos'] >= 15000) &
                        (df_movies['genero'].str.contains('action', case=False) &
                         df_movies['genero'].str.contains('adventure', case=False))]

df_filtered = df_filtered[['id', 'tituloPincipal', 'tempoMinutos', 'anoLancamento', 'genero', 'notaMedia', 'numeroVotos']]
df_filtered = df_filtered.groupby('tituloPincipal').first()
df_filtered = df_filtered.sort_values(by=['notaMedia', 'tempoMinutos'], ascending=[False, True])

# Definir lista para armazenar os resultados
filmes = []

# Definir URL base e chave da API
base_url = 'https://api.themoviedb.org/3/movie/'
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Definir barra de progresso
pbar = tqdm(total=len(df_filtered))

# Iterar sobre os IDs dos filmes filtrados
for movie_id in df_filtered['id']:
    # Construir a URL da API para obter as informações do país de produção do filme
    url = f'{base_url}{movie_id}?api_key={api_key}&language=pt-BR'
    
    # Fazer solicitação para a URL e obter os dados do filme
    response = requests.get(url)
    
    if response.status_code == 200:
        filme_data = response.json()
        
        # Extrair o nome do país de produção do filme
        countries = filme_data.get('production_countries', [])
        production_country = countries[0]['name'] if countries else 'N/A'
        
        # Adicionar a informação do país de produção ao dataframe
        df_filtered.loc[df_filtered['id'] == movie_id, 'production_country'] = production_country
        
        # Adicionar os dados do filme à lista de resultados
        filmes.append(filme_data)
    
    # Atualizar a barra de progresso
    pbar.update(1)
    
    #linha para teste abaixo
    # Parar a iteração após obter os 20 primeiros resultados
    #if len(filmes) >= 20:
    #    break

# Fechar a barra de progresso
pbar.close()

# Imprimir os dados obtidos
print(df_filtered.head(20).to_string(index=False))