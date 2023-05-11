import pandas as pd

# Carrega o arquivo CSV em um dataframe
df = pd.read_csv('actors.csv', encoding='utf=8')

# 4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
most_frequent_movies = df['#1 Movie'].value_counts().head(1)
print(f'O(s) filme(s) mais frequente(s) é(são) {most_frequent_movies.index[0]} com {most_frequent_movies.values[0]} ocorrências')
