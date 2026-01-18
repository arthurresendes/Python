"""
Raise -> Lança exceções 

OBS: O raise não é uma função e sim uma palavra reservado , como o def
"""

def cores(texto , cor):
    cores = ('verde', 'branco', 'azul', 'rosa')
    if type(texto) is not str:
        raise TypeError("Tem que ser string!!")
    if type(cor) is not str:
        raise TypeError("Tem que ser string!!")
    if cor not in cores:
        raise ValueError("Não esta na lista de cores!!")
    return texto + " " + cor


print(cores('Arthur' , 'azul'))