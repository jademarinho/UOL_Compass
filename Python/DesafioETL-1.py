with open('actors.csv', 'r') as file:
    lines = file.readlines()

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

#1- laço para procurar o ator com mais filmes
max_num_movies = 0
actor_with_max_movies = ''
for row in data:
    if int(row['Number of Movies']) > max_num_movies:
        max_num_movies = int(row['Number of Movies'])
        actor_with_max_movies = row['Actor']

print(f"O ator é {actor_with_max_movies} com {max_num_movies} filmes.")