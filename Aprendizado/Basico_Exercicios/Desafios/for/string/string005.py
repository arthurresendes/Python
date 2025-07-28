palavra = input("Digite uma palavra: ")
semEspaco = ""

for letra in palavra:
    if letra != " ":
        semEspaco += letra
   
print(f"String sem sem espaço: {semEspaco}")