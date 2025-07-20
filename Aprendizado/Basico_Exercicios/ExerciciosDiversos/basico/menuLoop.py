opcao = 0
itens = []

while opcao != 3:
    print("Menu: ")
    print("1- Cadastrar Item")
    print("2- Ver Item")
    print("3- Sair")
    opcao = int(input("Digite um numero: "))
    if opcao == 1:
        produto = input("Digite o produto que quer cadastrar: ")
        itens.append(produto)
    if opcao == 2:
        print("Lista de produtos: ")
        for produtos in itens:
            print(produtos)