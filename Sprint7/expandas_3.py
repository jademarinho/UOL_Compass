import pandas as pd

df = pd.read_csv('actors.csv', encoding='utf=8')

max_mean_per_movie = df.loc[df['Average per Movie'].idxmax()]
print(f'O ator/atriz com a maior média por filme é {max_mean_per_movie.Actor}')
