# Entrada: dois números

# Se o segundo for 0, capture o erro e mostre "Não é possível dividir por zero."

num = 0

while num < 1:
    try:
        num = int(input("Digite um numero: "))
        res = 10/num
    except ValueError:
        print("Digite um numero")
    except ZeroDivisionError:
        print("Numero nao se divide por zero")