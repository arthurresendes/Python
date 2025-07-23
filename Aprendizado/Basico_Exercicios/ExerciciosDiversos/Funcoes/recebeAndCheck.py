def verifica(num1):
    if num1 % 2 == 0:
        return 'par'
    else:
        return 'impar'

numero = int(input("Digite um numero: "))
print(verifica(numero))