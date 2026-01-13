def pedir_nome_senha() -> dict:
    while True:
        nome = input("Digite seu nome: ").title()
        senha = input("Digite a senha (diferente do nome): ").title()
        if nome != senha:
            return {'Nome': nome, 'Senha': senha}
        else:
            print("Digite a senha diferente do nome")


if __name__ == "__main__":
    print(pedir_nome_senha())