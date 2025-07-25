def multiplica_numerico(**kwargs):
    multiplica = 1
    for valor in kwargs.values():
        if not isinstance(valor , int) and not isinstance(valor , float):
            return "So aceitamos numeros"
        multiplica *= valor
    return multiplica

print(multiplica_numerico(num1 = 5 , num2 = 10))