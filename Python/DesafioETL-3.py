with open('etapa-3.txt', 'w') as file:
    with open('actors.csv', 'r') as data_file:
        lines = data_file.readlines()
        # Troca o nome do IronMan
        lines = [line.replace('"Robert Downey, Jr."', 'Robert Downey Jr.') for line in lines]
        headers = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            fields = line.strip().split(',')
            row = dict(zip(headers, fields))
            data.append(row)

        max_avg_movie = 0
        actor_with_best_avg = ''
        for row in data:
            if float(row['Average per Movie']) > max_avg_movie:
                max_avg_movie = float(row['Average per Movie'])
                actor_with_best_avg = row['Actor']

        result = f'O ator {actor_with_best_avg} com a media de faturamento de {max_avg_movie}\n'
        file.write(result)
        print(result)
