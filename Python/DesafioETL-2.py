with open('etapa-2.txt', 'w') as file:
    with open('actors.csv', 'r') as data_file:
        lines = data_file.readlines()
        # Arruma o nome do IronMan
        lines = [line.replace('"Robert Downey, Jr."', 'Robert Downey Jr.') for line in lines]
        headers = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            fields = line.strip().split(',')
            row = dict(zip(headers, fields))
            data.append(row)

        for row in data:
            actor = row['Actor']
            avg_per_movie = row['Average per Movie']
            result = f'{actor}: {avg_per_movie}\n'
            file.write(result)
            print(result)
