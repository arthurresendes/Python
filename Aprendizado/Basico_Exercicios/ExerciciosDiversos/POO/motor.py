class Motor:
    def __init__(self, potencia : int , tipo: str):
        self.potencia = potencia
        self.tipo = tipo
    
    def exibir_info(self):
        print(f"Motor: {self.tipo}, {self.potencia} cavalos de potência")

class Carro:
    def __init__(self ,marca: str , modelo: str ,motor: Motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}")
        self.motor.exibir_info()

moto1  = Motor(150, "Flex")

carro1 = Carro("Ford", "Focus",moto1)
carro1.exibir_info()