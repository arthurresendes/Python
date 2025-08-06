# Entrada: nome (str), idade (int)

# Tratar se a idade for inválida ou negativa 

while True:
    nome = input("Digite seu nome: ")
    if not nome.isalpha() or len(nome) < 3:
        print("Nome invalido!!")
    else:
        break


try:
    age = int(input("Digite sua idade: "))
    if age < 0:
        raise ValueError("Número negativo!!")
except ValueError:
    print("Digite numero!!")
else:
    print(nome , age)
finally:
    print("Fim da execução")