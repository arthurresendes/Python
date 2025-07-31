numeros = [1, 2, 3, 4, 5, 6]

def soPar(num):
    return num % 2 == 0

listagem = list(filter(soPar , numeros))
print(listagem)