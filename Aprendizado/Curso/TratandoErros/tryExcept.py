"""

Utilizamos o bloco try except para tratar erros que possam vir ocorrendo no nosso codigo , assim o programa pare de funcionar e o user receba uma msg de qual erro cometeu

try ->

execpt erro ->
"""

try:
    arthur()
except :
    print("Tivemos um problema")
    
try:
    len(5)
except TypeError as te:
    print(f"Erro -> {te}")

def pega_valor(dicionario,chave):
    return dicionario[chave]

dic = {'nome': 'Arthur'}
try:
    print(pega_valor(a, 'b'))
except KeyError as ke:
    print(f"Erro -> {ke}")
except NameError as ne:
    print(f"Erro -> {ne}")