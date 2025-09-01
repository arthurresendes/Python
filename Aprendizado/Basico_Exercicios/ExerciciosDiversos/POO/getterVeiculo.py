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

v1 = Veiculo('Fusca', 2001)
print(v1.get_modelo())
print(v1.set_modelo(2020))
print(v1.info())