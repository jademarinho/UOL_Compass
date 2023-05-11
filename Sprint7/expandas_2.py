import pandas as pd

df = pd.read_csv('actors.csv', encoding='utf=8')

movies_mean = df['Number of Movies'].mean()
print(f'A média do número de filmes é {movies_mean}')