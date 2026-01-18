'''
JSON

JSON - JavaScript Object Notation
encode - na escritura
decode - leitura
jsonpickle.encode/decote
'''
import json

ret = json.dumps(['produtos' , {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)

class Gato:
    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca

feliz = Gato('Felix', 'Felino')

ret2 = json.dumps(feliz.__dict__)
print(ret2)

'''
with open('felix.json', 'w') as file:
    ret3 = jsonpickle.encode(felix)
    file.write(ret3)
'''