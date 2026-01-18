'''
Metodos magicos são todos metodos dunder (__x__)

__repr__ = Representação do objeto
__str__ = retorna uma string/self.x
__len__ = Serve para ler tamanhos ou qtd de algo em classe
__del__ = Deletar


'''

class Livro:
    def __init__(self,titulo: str,autor: str,paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"
    
    def __str__(self):
        return self.titulo
    
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Um objeto do tipo livro foi deletado')

livro1 = Livro('Python' , 'Arthur', 220)
livro2 = Livro('C' , 'Arthur', 520)

print(livro1)
print(livro2)
print(len(livro1))