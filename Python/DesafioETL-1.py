with open('etapa-1.txt', 'w') as file:
    with open('actors.csv', 'r') as data_file:
        lines = data_file.readlines()
        headers = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            fields = line.strip().split(',')
            if len(fields) == len(headers):
                row = dict(zip(headers, fields))
                if '"' in row['Actor']:
                    row['Actor'] = row['Actor'].strip('"') + ', ' + row['Total Gross']
                    row['Total Gross'] = fields[2]
                    data.append(row)
                data.append(row)

        max_num_movies = 0
        actor_with_max_movies = ''
        for row in data:
            if int(row['Number of Movies']) > max_num_movies:
                max_num_movies = int(row['Number of Movies'])
                actor_with_max_movies = row['Actor']

        result = f"O ator {actor_with_max_movies} com {max_num_movies} filmes."
        file.write(result)
        print(result)