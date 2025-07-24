while True:
    try:
        numero = int(input("Digite um numero de 1 a 5: "))
        if numero > 0 and numero < 6:
            print(numero)
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite apenas números.")