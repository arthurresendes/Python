class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adicionar_prod(self, produto: str):
        self.produtos.append(produto)
        
    def remover_prod(self, produto: str):
        if produto in self.produtos:
            self.produtos.remove(produto)
    
    def mostrar(self):
        print("Seu carrinho: ")
        for i in self.produtos:
            print(i)

c1 = Carrinho()
c1.adicionar_prod('Cafe')
c1.adicionar_prod('Fini')
c1.adicionar_prod('Coca-Cola')
c1.remover_prod('Fini')
c1.mostrar()