class Animal:
    contador = 0
    def __init__(self,nome):
        self.__contador = Animal.contador + 1
        self.__nome = nome
        Animal.contador = self.__contador

    def apresenta(self):
        return f"O animal é {self.__nome} e já temos {self.__contador} animais na nossa classe"

ani1 = Animal('Cachorro')
ani2 = Animal('Gato')
ani3 = Animal('Passaro')
print(ani1.apresenta())
print(ani2.apresenta())
print(ani3.apresenta())