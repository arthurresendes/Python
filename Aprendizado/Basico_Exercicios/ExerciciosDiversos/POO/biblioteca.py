class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self , livro: str):
        self.livros.append(livro)
    
    def remover_livros(self, livro: str):
        if livro in self.livros:
            self.livros.remove(livro)
    
    def listar(self):
        print("Livros na nossa biblioteca: ")
        for i in self.livros:
            print(i)

l1 = Biblioteca()

l1.adicionar_livro("Homem aranha")
l1.adicionar_livro('Senhor dos aneis')
l1.remover_livros('Homem aranha')
l1.listar()