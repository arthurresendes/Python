"""
While percorre enquanto a condição for True
"""

numero  = 1

while numero < 10:
    print(numero)
    numero += 1
    
print('\n')

resposta = ""

while resposta != "sim":
    resposta = input("Digite sim para o loop parar: ").lower()