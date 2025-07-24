assentos = ['Livre', 'Livre', 'João', 'Livre', 'Ana']

 

def menu():

    print('-----------------------------')

    print("Seja bem vindo ao CinemaPy")

    print('-----------------------------')

 

 

def perguntas():

    nome = input("Digite seu nome: ").title()

    print(assentos)

   

    while True:

        try:

            escolha = int(input("Escolha um assento de 1 a 5: ")) - 1

 

            if escolha < 0 or escolha >= len(assentos):

                print("Número de assento inválido.")

            elif assentos[escolha] != 'Livre':

                print("O assento já está ocupado por", assentos[escolha])

            else:

                assentos[escolha] = nome

                print("Assento reservado com sucesso!")

                break

        except ValueError:

            print("Digite apenas números válidos.")

 

    print("Assentos finais:", assentos)

   

    

 

def main():

    menu()

    perguntas()

   

main()