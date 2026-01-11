def contagem(frase: str) -> list[int,str]:
    palavras = frase.split()
    contador_palavras = len(palavras)
    
    palavra_mais_utilizada = max(set(palavras), key=palavras.count)
    return [contador_palavras,palavra_mais_utilizada]


print(contagem("Ola mundo O mundo é divertido"))