"""
Tipo string

"""

nome = 'Arthur Resende'
print(nome.upper())
print(type(nome))

# Slice de string 
print(nome[0:6]) # Do zero ate o 6 (Primeiro nome)
print(nome[7:15]) # Do 7 ate o 15 (sobrenome)

#Inverte o nome ao contrario
print(nome.lower()[::-1])

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

#Como nesse split foi didvidio em 2 [Arthur , Gomes] caso queira acessar um dos elementos ele começara na contagem 0 , no caso Arthur = 0 , podendo ser escrito nome.split(0) e retornaria Arthur ou nome.split(1) voltaria Gomes



