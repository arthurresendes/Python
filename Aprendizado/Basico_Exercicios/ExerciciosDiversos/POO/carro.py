class Carro:
    cont = 0
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.cont += 1

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")
    
    @classmethod
    def mostraQuantos(cls):
        return cls.cont

car1 = Carro('Fusca', 'Volkswagen', 1980)

car1.exibir_detalhes()

print(Carro.mostraQuantos())