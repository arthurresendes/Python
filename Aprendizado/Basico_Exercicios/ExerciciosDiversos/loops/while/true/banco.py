saldo = 0

 

 

while True:

    try:

        escolha = int(input("1-Ver saldo\n2-Depositar\n3-Sair\n"))

        if escolha == 3:

            break

        elif escolha == 1:

            print(f"Seu saldo é de {saldo}")

        elif escolha == 2:

            valor = float(input("Digite o valor a se depositar: "))

            saldo = valor + saldo

        else:

            print("Numero não foi escolhido corretamente!!")

   

    except ValueError:

        print("Caractere digitado invalido")