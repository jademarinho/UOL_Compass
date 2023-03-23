import json

with open('person.json') as arquivo:
    dados_json = arquivo.read()
    dados = json.loads(dados_json)

print(dados)