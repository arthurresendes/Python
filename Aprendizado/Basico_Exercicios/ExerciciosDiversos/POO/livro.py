class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir(self):
        return f"Titulo {self.titulo}\n Autor: {self.autor}\nAno:{self.ano}"


lv1 = Livro("Clean code", 'Jose', 2008)
lv2 = Livro('Diario de um banana', 'Jeff' , 2012)


print(lv1.exibir())
print(lv2.exibir())

