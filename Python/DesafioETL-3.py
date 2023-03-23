with open('actors.csv', 'r') as file:
    lines = file.readlines()

# Troca o nome do ironman
lines = [line.replace('"Robert Downey, Jr."', 'Robert Downey Jr.') for line in lines]

headers = lines[0].strip().split(',')
data = [] #Armazenar o dicionario

for line in lines[1:]:
    fields = line.strip().split(',')
    row = dict(zip(headers, fields))
    data.append(row)


max_avg_movie = 0
actor_with_best_avg: ''
for row in data:
    if float(row['Average per Movie']) > max_avg_movie:
        max_avg_movie = float(row['Average per Movie'])
        actor_with_best_avg = row['Actor']

print(f'O ator é {actor_with_best_avg} com a média de faturamento de {max_avg_movie}')