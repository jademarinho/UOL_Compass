with open('actors.csv', 'r') as file:
    lines = file.readlines()

""" CODIGO QUE DEU ERRO. 
headers = lines[0].strip().split(',')
data = [] #Armazenar o dicionario
# laço para ler as linhas e tratar o ", " do Iron Man.
for line in lines[1:]:
    fields = line.strip().split(',')
    if len(fields) == len(headers):
        row = dict(zip(headers, fields))
        if '"' in row['Actor']:
            row['Actor'] = row['Actor'].strip('"') + ', ' + row['Total Gross']
            row['Total Gross'] = fields[2]
            data.append(row)
        data.append(row)
        
"""
lines = [line.replace('"Robert Downey, Jr."', 'Roberts Downey Jr.') for line in lines]

headers = lines[0].strip().split(',')
data = [] #Armazenar o dicionario

for line in lines[1:]:
    fields = line.strip().split(',')
    row = dict(zip(headers, fields))
    data.append(row)

####################

print(data)
#1- laço para procurar o ator com mais filmes
max_num_movies = 0
actor_with_max_movies = ''
for row in data:
    if int(row['Number of Movies']) > max_num_movies:
        max_num_movies = int(row['Number of Movies'])
        actor_with_max_movies = row['Actor']

print(f"O ator é {actor_with_max_movies} com {max_num_movies} filmes.")

#2- laço para ler o row Actor e AVG per movie.
for row in data:
    actor = row['Actor']
    avg_per_movie = row['Average per Movie']

    print(f'{actor}: {avg_per_movie}')

#3- laço para ator com maior avg per movie.
max_avg_movie = 0
actor_with_best_avg: ''
for row in data:
    if float(row['Average per Movie']) > max_avg_movie:
        max_avg_movie = float(row['Average per Movie'])
        actor_with_best_avg = row['Actor']

print(f'O ator é {actor_with_best_avg} com a média de faturamento de {max_avg_movie}')


#4- filmes mais frequentes.

count_pop_movie = {}
for row in data:
    if row['#1 Movie'] in count_pop_movie:
        count_pop_movie[row['#1 Movie']] += 1
    else:
        count_pop_movie[row['#1 Movie']] = 1

pop_movie = max(count_pop_movie, key=count_pop_movie.get)
num_pop_movie = count_pop_movie[pop_movie]

print(f'{pop_movie}: {num_pop_movie}')

#5-
order_by_gross = sorted(data, key=lambda x: float(x['Total Gross']), reverse=True)

for actor in order_by_gross:
    print(f"{actor['Actor']}: {actor['Total Gross']}")