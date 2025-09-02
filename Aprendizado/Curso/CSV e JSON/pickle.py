'''
Conhecendo o pickle

wb , rb
Objeto python -> Binarização

binarização -> Objeto Python
'''
import pickle

class Animal:
    def __init__(self,nome):
        self._nome = nome
    
    def comer(self):
        print(f"O animal {self._nome} gosta de comer")

class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    
    def mia(self):
        print(f"O {self._nome} mia")

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    
    def latir(self):
        print(f"O {self._nome} late")

felix = Gato('Felix')
pluto = Cachorro('Pluto')
with open('animais.pickles', 'wb') as file:
    pickle.dump((felix,pluto),file)
# Dump recebe dois parametros