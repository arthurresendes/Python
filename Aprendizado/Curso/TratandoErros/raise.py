"""
Raise -> Lança exceções 

OBS: O raise não é uma função e sim uma palavra reservado , como o def
"""

def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError("Número não se divide por zero!")
    return a /b

print(dividir(1,0))