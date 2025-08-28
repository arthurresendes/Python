class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")

car1 = Carro('Fusca', 'Volkswagen', 1980)

car1.exibir_detalhes()