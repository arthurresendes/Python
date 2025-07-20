palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

if len(palavra1) != len(palavra2):
    print("As palavras não são anagramas")
else:
    if sorted(palavra1) == sorted(palavra2):
        print("As palavras são anagramas")
    else:
        print("As palavras tem a mesma quantidade , mas tem letras diferentes")