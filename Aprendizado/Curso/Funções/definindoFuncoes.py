"""
Definindo funções

Funções são pequenos trechos de codigo que realizam tarefas especificas

Parametros de entrada são opcionais , onde tendo mais de um cada , um separado por virgula podenso ser opcional ou não

def nome_que_quiser(parametros):

nome_que_quiser(parametros)

"""

#Exemplo:
def borda():
    print("---------------------------------------------")

# Exemplo de utilização de funções:

cores = ['azul' , 'verde' , 'roxo' , 'azul' , 'amarelo']

# Utilizando função integrada , chamada de built-in do py print
borda()
print(cores)
borda()

# Em python se define a função da seguinte forma: def nome_que_quiser(parametros):

def diz_oi():
    print("Oi")

diz_oi()

def diz_oi_nome(nome):
    print(f"Ola , {nome}")

seuNome = input("Digite seu nome: ")
diz_oi_nome(seuNome)

def cantar_parabens():
    print("Parabens para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")

for i in range(5):
    cantar_parabens()

canta = cantar_parabens

canta()