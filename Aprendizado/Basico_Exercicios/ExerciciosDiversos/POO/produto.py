class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    def calcular_total(self):
        return f"Preço total: {self.preco * self.quantidade}"

    def exibir_produto(self):
        return f"Produto: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}"

prod1 = Produto('Café', 10.20, 3)
print(prod1.exibir_produto())
print(prod1.calcular_total())

prod2 = Produto('Fini', 6.20, 2)
print(prod2.exibir_produto())
print(prod2.calcular_total())