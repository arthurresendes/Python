"""
*args

Serve para passar varios parametros em um so ou passar nenhum


"""

def diz_oi(*nome):
    return f"Oi! {nome}"


print(diz_oi('Arthur' , 'Jose' , 'Maria'))

def number(*numeros):
    return sum(numeros)


numeros  = [1,2,3,4,5,6,7,8,9]


# O Python entende: essa função pode receber vários valores como argumentos posicionais, e todos eles serão guardados dentro de uma tupla chamada numeros.

print(number(*numeros))