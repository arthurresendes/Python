class Veiculo:
    def __init__(self , marca:str , ano:int , modelo) -> None:
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
   
class Carro(Veiculo):
    def __init__(self,marca,ano,modelo,portas):
        self.portas = portas
        super().__init__(marca,ano,modelo)
   
    def mostrar_info(self):
        return f"Carro da {self.marca} do ano {self.ano} do modelo {self.modelo} com {self.portas} portas"

class Moto(Veiculo):
    def __init__(self,marca,ano,modelo,cilindradas):
        self.cilindradas = cilindradas
        super().__init__(marca,ano,modelo)
   
    def mostrar_info(self):
        return f"Carro da {self.marca} do ano {self.ano} do modelo {self.modelo} com {self.cilindradas} cilindradas"


car1 = Carro('Fusca' , 2000, 'Antigo', '2')
mot1 = Moto('Kawasaki', 2025, 'Nova', 160)
print(car1.mostrar_info())
print(mot1.mostrar_info())
