class Veiculo:
    def __init__(self, marca , modelo):
        self.marca = marca
        self.modelo = modelo

    def  get_modelo(self):
        return self.modelo

    def set_modelo(self,m):
        self.modelo = m
        return m
    def info(self):
        return f"Marca: {self.marca} Modelo: {self.modelo}"

class Carro(Veiculo):
    def __init__(self,marca,modelo, porta):
        super().__init__(marca,modelo)
        self.porta = porta

    def get_porta(self):
        return self.porta

    def set_porta(self,m):
        self.porta = m
        return m

    def info(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Portas: {self.porta}"

car1 = Carro('Fusca', 2002, 2)
print(car1.get_porta())
print(car1.set_porta(4))
print(car1.info())