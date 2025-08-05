def nome(name):
    if not isinstance(name , str):
        raise TypeError("Nome tem que ser string")
    if len(name) < 3:
        raise ValueError("Nome Curto demais!!")
    return name

n = input("Digite seu nome: ")
print(nome(n))