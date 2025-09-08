def media(lista: list) -> float:
    soma = 0
    for i in lista:
        soma = i + soma
    media =  soma/ len(lista)
    return f"A media eh {media}"

print(media([10.0,10.0,2.2,6.6,4.7]))
print(media.__annotations__)