import pandas as pd

df = pd.read_csv('actors.csv', encoding='utf=8')

most_frequent_movies = df['#1 Movie'].value_counts().head(1)
print(f'O(s) filme(s) mais frequente(s) é(são) {most_frequent_movies.index[0]} com {most_frequent_movies.values[0]} ocorrências')
