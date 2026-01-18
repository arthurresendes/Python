'''

__ é um metodo que faz ficar privado e ser consultado apenas dentro da propria classe


'''

class Lampada:
    def __init__(self,voltagem,cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    imposto = 1.05
    contador = 0
    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Cafe', 'Cafeina' , 10)
print(p1.id)
print(p1.valor)
p2 = Produto('Cafe', 'Cafeina' , 30)
print(p2.id)
print(p2.valor)


print(p1.__dict__)
print(p2.__dict__)

del p2.valor
print(p2.__dict__)