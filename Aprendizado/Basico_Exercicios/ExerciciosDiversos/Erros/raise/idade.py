def idade(age):
    if age < 0:
        raise ValueError("Sua idade não pode ser menor que 0")
    return age

anos = int(input("Digite sua idade: "))
print(idade(anos))