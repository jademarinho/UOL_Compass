import requests

# Criar uma lista de URLs únicas com base nos IDs dos filmes filtrados
api_key = "XXXXXXXXXXXXXXXXXXXXXXX"
urls = set()

for movie_id in df_filtered['id'].head(20):  # Selecionar os 20 primeiros IDs
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=pt-BR'
    urls.add(url)

# Criar uma lista para armazenar os dados dos filmes
filmes = []

# Fazer solicitações para as URLs e obter os dados dos filmes
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        filme_data = response.json()
        filmes.append(filme_data)

# Mostrar os dados dos filmes e outras informações interessantes
for filme in filmes:
    print("ID:", filme["id"])
    print("Título:", filme["title"])
    print("País de Origem:", filme["production_countries"][0]["name"])
    print("Gêneros:", [genre["name"] for genre in filme["genres"]])
    print("Data de Lançamento:", filme["release_date"])
    print("Resumo:", filme["overview"]) 
    print("Nota Média:", filme["vote_average"])
    print("Número de Votos:", filme["vote_count"])
    print("--------------------")