def conta_vogais(texto:str)-> int:
    vogais = ['a', 'e', 'i', 'o', 'u']
    return len(list(filter(lambda letra: letra.lower() in vogais, texto)))