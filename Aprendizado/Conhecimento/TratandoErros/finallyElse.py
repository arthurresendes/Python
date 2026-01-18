"""
try / except / else / finally

Toda entrada de usuario deve ser tradado 

"""

try:
    num = int(input("Digite um numero: "))
except ValueError as ve:
    print(f"Erro -> {ve}")
else:
    print(num)
finally:
    print("Fim execução")


def dividir(a,b):
    try:
        return int(a) / int (b)
    except(ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'

try:
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))

except (ValueError,NameError):
    print("Erro!!")

else:
    print(dividir(n1,n2))

