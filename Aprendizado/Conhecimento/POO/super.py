'''
Super em pyhton

'''
class Animal:
    def __init__(self , nome , especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")

class Gato(Animal):
    def __init__(self , nome , especie , raca):
        super().__init__(nome,especie)
        super().faz_som('Miau')
        self.__raca = raca

gat1 = Gato('Floquinho', 'Felino', 'Persa')
gat1.faz_som('miau')