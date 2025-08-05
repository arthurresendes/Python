def verifica(texto):
    if not isinstance(texto,str):
        raise TypeError("O seu texto não eh uma string")    
    return texto

text = input("Digite uma palavra: ")
print(verifica(text))