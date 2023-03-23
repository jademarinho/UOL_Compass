with open('actors.csv', 'r') as file:
    lines = file.readlines()

lines = [line.replace('"Robert Downey, Jr."', 'Roberts Downey Jr.') for line in lines]

headers = lines[0].strip().split(',')
data = [] #Armazenar o dicionario

for line in lines[1:]:
    fields = line.strip().split(',')
    row = dict(zip(headers, fields))
    data.append(row)

print(data)



count_pop_movie = {}
for row in data:
    if row['#1 Movie'] in count_pop_movie:
        count_pop_movie[row['#1 Movie']] += 1
    else:
        count_pop_movie[row['#1 Movie']] = 1

pop_movie = max(count_pop_movie, key=count_pop_movie.get)
num_pop_movie = count_pop_movie[pop_movie]

print(f'{pop_movie}: {num_pop_movie}')
