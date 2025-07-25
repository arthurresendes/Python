def atualiza_estoque(**itens):
    resultado = ""
    nomes = itens['nome']
    quantidades = itens['qtd']
    precos = itens['preco']

    for i in range(len(nomes)):
        subtotal = quantidades[i] * precos[i]
        resultado += (
            f"Produto: {nomes[i]}\n"
            f"Quantidade: {quantidades[i]}\n"
            f"Preço unitário: R$ {precos[i]}\n"
            f"Subtotal: R$ {subtotal}\n"
            f"{'-'*30}\n"
        )
    return resultado


print(atualiza_estoque(
    nome=['Cafe', 'Candida'],
    qtd=(5, 10),
    preco=(20, 5)
))