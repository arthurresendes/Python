def cadastro(**user):
    if user['nome'] == "" or user['email'] == "":
        return 'Dados não preenchidos'
    return f"Nome:{user['nome']}\nEmail:{user['email']}"

name = input("Digite seu nome: ")
seuEmail = input("Digite seu email: ")

print(cadastro(nome = name , email = seuEmail))