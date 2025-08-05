"""
Erros mais comuns em python


Traceback -> Saída de erro 
NameError -> Palavra errada, falta de condições
ZeroDivisionError -> Divisão por zero
SintaxError -> Erro de sintaxe
TypeError -> Ação para o tipo errado , str em ints , vice-versa, etc
IndexError -> Busca em posições inexistentes
ValueError ->  Usar int em string , strings em int , etc
KeyError -> Quando tentamos acessar uma chave em um dicionario que não existe 
AtributeError -> Não existe tal função para quele determinada variavel 
IdentationError -> Ocorre quando não se respeita a indentação do py que eh de 4 espacos 

"""

'''NameError: '''
#printf("Arthur Resende")

'''ZeroDivisionError'''
'''
def nums(a, b):
    return a/b

print(nums(6,0))
'''

'''SintaxeError'''
'''
print("Ola,Mundo)

'''

'''TypeError'''
'''
print(len(5))
'''

'''IndexError'''
'''
lista = ['ARG']
print(lista[0][10])
'''

'''ValueError'''
'''
print(int("Arthur"))
'''

'''KeyError'''
'''
dict{}
print(dict['oi'])
'''

'''AtributeError'''
'''
tupla = (11,2,31,4)
print(tupla.sort())
'''

'''IdentationError'''
'''
age = 18
if age == 18:
print("Legal")
'''