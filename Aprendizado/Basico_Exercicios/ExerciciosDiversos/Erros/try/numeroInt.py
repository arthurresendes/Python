# Entrada: valor digitado

# Se for inválido, mostre "Digite apenas números inteiros."

num = None

while type(num) is not int:
    try:
        num = int(input("Digite um numero: "))
    except ValueError:
        print("Digite um valor numerico inteiro!!")
print(num)