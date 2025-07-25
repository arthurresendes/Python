def mostra_indice(*itens):
    for indice , valor in enumerate(itens):
        print(f"Item {indice}: {valor}")

mostra_indice("Ola" , "Oi", "Hello")