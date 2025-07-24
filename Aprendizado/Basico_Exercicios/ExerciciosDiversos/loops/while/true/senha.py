tentativa = 0

 

while True:

    try:

        print("A senha é python123")

        senha = input("Digite a senha: ")

        if senha != 'python123':

            tentativa = tentativa + 1

            print(f"Você tem mais {3-tentativa} tentativas")

            if tentativa == 3:

                print("Bloqueado")

                break

        else:

            print("Acesso liberado!!")

   

    except ValueError:

        print("Caractere digitado invalido")