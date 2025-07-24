def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra in "aeiou":
            contador +=1
    return contador

palavra = input("Digite uma palavra: ").lower()
print(contar_vogais(palavra))