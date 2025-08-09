num1 = int(input("Digite num1: "))
num2 = int(input("Digite num2: "))

while True:
    operacao = input("Digite uma das operações(+,-,*,/): ")
    if operacao == '+':
        print(num1 + num2)
        break
    elif operacao == '-':
        print(num1-num2)
        break
    elif operacao == '*':
        print(num1*num2)
        break
    elif operacao == '/':
        print(float(num1/num2))
        break
    else:
        print("Operação não encontrada!!")