"""
Item: com nome e preco.

Pedido: que tem uma lista de itens e métodos para:

adicionar item

calcular valor total do pedido

listar os itens

👉 O pedido é composto de vários itens
"""


class Item:
    contador = 0
    def __init__(self, nome: str, preco: float):
        self.id = Item.contador + 1
        self. nome = nome
        self.preco = preco
        Item.contador = self.id
    
    def item(self):
        print(f"Produto: {self.nome} - Preço: {self.preco}")
    
    def valores(self):
        return self.preco


class Produto:
    def __init__(self):
        self.items = []
    
    def adicionar_item(self, item: Item):
        self.items.append(item)
    
    def calcular_items(self):
        soma = 0.0
        for i in self.items:
            soma += i.valores()
        print(f"A soma de todos os items é de {soma:.2f}")
    
    def listar_items(self):
        for i in self.items:
            i.item()

it1  = Item('Cafe', 20.20)
it2  = Item('Fini', 12.20)
it3  = Item('Arroz', 20.20)
prod = Produto()
prod.adicionar_item(it1)
prod.adicionar_item(it2)
prod.adicionar_item(it3)
prod.listar_items()
prod.calcular_items()
