num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
funcao = lambda x, y:  x
funcao1 = lambda x, y: y

if num1 > num2:
    print(funcao(num1,num2))
else:
    print(funcao1(num1,num2))