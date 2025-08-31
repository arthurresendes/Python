class Veiculo:
    def __init__(self,marca: str , ano: int):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca: str , ano: int , num_portas:int , tipo_combustivel:str):
        super().__init__(marca,ano)
        self.num_portas = num_portas
        self.tipo_combustivel = tipo_combustivel
    
    def apresentar(self):
        return f"Esse carro é do ano {self.ano} da marca {self.marca} com {self.num_portas} portas e o combustivel do tipo {self.tipo_combustivel}"

class Moto(Veiculo):
    def __init__(self, marca: str , ano: int , cilindrada:str , tipo:str):
        super().__init__(marca,ano)
        self.cilindrada = cilindrada
        self.tipo = tipo
    
    def apresentar(self):
        return f"Essa moto é do ano {self.ano} da marca {self.marca} com {self.cilindrada} cilindradad e do tipo {self.tipo}"


car = Carro('Ferrari' , 2010, 4,'Etanol')
print(car.apresentar())
moto = Moto('Kawasaki' , 2020,'150cc','esportiva')
print(moto.apresentar())