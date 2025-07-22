from collections import Counter as ct

texto = "baixar"
vogais = "aeiouAEIOU"

vogais_na_palavra = [letra for letra in texto if letra in vogais]

contador = ct(vogais_na_palavra)

print(contador)