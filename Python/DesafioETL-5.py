with open('actors.csv', 'r') as file:
    lines = file.readlines()

lines = [line.replace('"Robert Downey, Jr."', 'Roberts Downey Jr.') for line in lines]

headers = lines[0].strip().split(',')
data = [] #Armazenar o dicionario

for line in lines[1:]:
    fields = line.strip().split(',')
    row = dict(zip(headers, fields))
    data.append(row)

order_by_gross = sorted(data, key=lambda x: float(x['Total Gross']), reverse=True)

with open('etapa-5.txt', 'w') as output_file:
    for actor in order_by_gross:
        output_file.write(f"{actor['Actor']}: {actor['Total Gross']}\n")