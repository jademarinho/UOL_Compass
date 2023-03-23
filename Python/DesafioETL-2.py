with open('actors.csv', 'r') as file:
    lines = file.readlines()

# Arruma o nome do IronMan
lines = [line.replace('"Robert Downey, Jr."', 'Roberts Downey Jr.') for line in lines]

headers = lines[0].strip().split(',')
data = [] #Armazenar o dicionario

for line in lines[1:]:
    fields = line.strip().split(',')
    row = dict(zip(headers, fields))
    data.append(row)



#2- laço para ler o row Actor e AVG per movie.
for row in data:
    actor = row['Actor']
    avg_per_movie = row['Average per Movie']

    print(f'{actor}: {avg_per_movie}')
