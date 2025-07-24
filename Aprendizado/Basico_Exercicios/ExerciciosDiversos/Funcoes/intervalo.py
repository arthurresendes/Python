def intervalo(numero , inicio = 0, fim = 100):
    if numero > 0 and numero < 101:
        return "Esta no intervalo"
    else:
        return "Não esta no intervalo"

num =  int(input("Digite um numero: "))
print(intervalo(num))