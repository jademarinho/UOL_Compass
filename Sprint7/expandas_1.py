import pandas as pd

# Carrega o arquivo CSV em um dataframe
df = pd.read_csv('actors.csv', encoding='utf=8')

# 1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
max_movies = df.loc[df['Number of Movies'].idxmax()]
print(f'O ator/atriz com o maior número de filmes é {max_movies.Actor} com {max_movies["Number of Movies"]} filmes')