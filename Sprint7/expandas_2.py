import pandas as pd

# Carrega o arquivo CSV em um dataframe
df = pd.read_csv('actors.csv', encoding='utf=8')

# 2. Apresente a média da coluna contendo o número de filmes.
movies_mean = df['Number of Movies'].mean()
print(f'A média do número de filmes é {movies_mean}')