from collections import Counter as ct

texto = "python é incrível e python é divertido"

frase = texto.split()
print(frase)

contador = ct(frase)
print(contador)