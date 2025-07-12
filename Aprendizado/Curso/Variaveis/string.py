"""
Tipo string

"""

nome = 'Arthur Resende'
print(nome.upper())
print(type(nome))

nome = "arthur's bar" #Para usar ' em um texto precisa estar em aspas dupla 
print(nome.title())
print(type(nome))

nome = 'Arthur \nGomes' #\n funciona em py tambem para quebrar linha
print(nome.lower())
print(type(nome))

nome = """Arthur
Gomes"""  #Outro metodo de pular linha com aspas duplas triplas
print(nome.split()) # Split transformo as palavras em lista
print(type(nome))



