numeros = list(range(1, 51))

def divisor(num):
    if num % 3 == 0 or num % 5 == 0:
        return num

listagem = list(filter(divisor , numeros))
print(listagem)