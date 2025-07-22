from collections import Counter as ct

palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

verifica1 = ct(palavra1)
verifica2 = ct(palavra2)

if verifica1 ==  verifica2:
    print("Palavras tem o mesmo tamanho")
    if sorted(verifica1) == sorted(verifica2):
        print("São anagramas")
else:
    print("Palavras de tamanho diferente")
