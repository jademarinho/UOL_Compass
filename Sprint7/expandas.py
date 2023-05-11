import pandas as pd

df = pd.read_csv('actors.csv', encoding='utf=8')

max_movies = df.loc[df['Number of Movies'].idxmax()]
print(f'O ator/atriz com o maior número de filmes é {max_movies.Actor} com {max_movies["Number of Movies"]} filmes')

movies_mean = df['Number of Movies'].mean()
print(f'A média do número de filmes é {movies_mean}')

max_mean_per_movie = df.loc[df['Average per Movie'].idxmax()]
print(f'O ator/atriz com a maior média por filme é {max_mean_per_movie.Actor}')

most_frequent_movies = df['#1 Movie'].value_counts().head(1)
print(f'O(s) filme(s) mais frequente(s) é(são) {most_frequent_movies.index[0]} com {most_frequent_movies.values[0]} ocorrências')
