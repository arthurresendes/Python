print(palavra := input("Digite uma palavra: "))
resultado = [maiusculo for letra in palavra if (maiusculo := letra.upper()) and maiusculo in "AEIOU"]
print(resultado)