cadastro = {
    "nome": input("Digite seu nome: "),
    "senha": input("Digite sua senha: ")
}

print("Bem-vindo as lojas Arthur&Arthur")
print("Vamos fazer o login")
confirmaNome = input("Confirme seu nome: ")
while confirmaNome != cadastro["nome"]:
    confirmaNome = input("Nome incorreto , digite novamente: ")

tentativas = 1
confirmaSenha = input("Confirme sua senha: ")
while confirmaSenha != cadastro["senha"]:
    confirmaNome = input("Senha incorreta , digite novamente: ")
    tentativas += 1
    if tentativas == 3:
        print("Limite de tentivas , bloqueado")
        break

print("Login aprovado")