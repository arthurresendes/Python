num = int(input("Digite um num: "))
verifica= lambda x:x % 3 == 0 or x % 5 == 0
print(verifica(num))