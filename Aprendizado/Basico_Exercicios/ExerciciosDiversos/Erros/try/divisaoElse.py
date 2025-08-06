# Entrada: a e b

# try/except para divisão por zero

# else para exibir o resultado


try:
    a = int(input("Digite o numero 1: "))
    b = int(input("Digite o numero 2: "))
    res = a/b

except ValueError:
    print("Digite numeros inteiros validos!!")

except ZeroDivisionError:
    print("Número não se divide por zero!!")

else:
    print(res)