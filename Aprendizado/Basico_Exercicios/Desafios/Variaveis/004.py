palavra = input("Digite uma palavra para verificar se ela eh palindromo: ")

palavraInverte = palavra.lower()[::-1]

if palavra == palavraInverte: 
    print(f"Eh palindromo. Sua palavra: {palavra} , palavra ao contrario:      {palavraInverte} ")
else:
    print(f"Nao eh palindromo.Sua palavra:{palavra} , palavra ao contrario: {palavraInverte}")