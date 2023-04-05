with open('estudantes.csv', 'r', encoding='utf-8') as file:
    estudantes = [tuple(line.strip().split(',')) for line in file]

maiores_notas = lambda notas: sorted(notas, reverse=True)[:3]

media_notas = lambda notas: round(sum(maiores_notas(notas)) / 3, 2)

for estudante in sorted(estudantes):
    nome = estudante[0]
    notas = list(map(int, estudante[1:]))
    maiores = maiores_notas(notas)
    media = media_notas(notas)
    print(f"Nome: {nome} Notas: {maiores} Média: {media}")

