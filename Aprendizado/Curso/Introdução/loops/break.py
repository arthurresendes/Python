for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")

while True:
    comando = input('Digite sair para sair: ').lower()
    if comando == 'sair':
        print("Acertou o comando!!")
        break
    else:
        print("Tente novamente!!\n")