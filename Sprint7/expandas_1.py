import pandas as pd

df = pd.read_csv('actors.csv', encoding='utf=8')

max_movies = df.loc[df['Number of Movies'].idxmax()]
print(f'O ator/atriz com o maior número de filmes é {max_movies.Actor} com {max_movies["Number of Movies"]} filmes')