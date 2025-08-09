print("Vamos verificar o dia de rodizio do seu carro!!")
while True:
    placa = input("Digite a placa do seu carro: ")
    if placa[-1] == '1' or placa[-1] == '2':
        print("Seu rodizio eh segunda")
        break
    elif placa[-1] == '3' or placa[-1] == '4':
        print("Seu rodizio eh terca")
        break
    elif placa[-1] == '5' or placa[-1] == '6':
        print("Seu rodizio eh quarta")
        break
    elif placa[-1] == '8' or placa[-1] == '7':
        print("Seu rodizio eh quinta")
        break
    elif placa[-1] == '9' or placa[-1] == '0':
        print("Seu rodizio eh sexta")
        break
    else:
        print("Invalido!!")