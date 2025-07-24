while True:

    try:

        sair = input("Se deseja sair , digite 'sair' , se não digite qualquer string: ").lower()

        if sair == 'sair':

            break

        num1 = int(input("Digite um numero: "))

        num2 = int(input("Digite outro numero: "))

        operacao = input("Escolha uma das operações(+,-,*,/): ")

        if operacao == '+':

            print(num1+num2)

        elif operacao == '-':

            print(num1-num2)

        elif operacao == '*':

            print(num1 *num2)

        elif operacao == '/':

            print(num1 / num2)

        else:

            print("Não foi encontrado uma operação, tente novamente!")

   

    except ValueError:

        print("Caractere digitado invalido")