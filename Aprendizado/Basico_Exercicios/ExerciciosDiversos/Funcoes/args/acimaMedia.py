def acima_media(*numerosMedia):
    lista = []
    for num2 in numerosMedia:
        if num2 >= 6:
            lista.append(num2)
    return lista

print(acima_media(1,6,8,5,9,2))