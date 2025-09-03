'''
Manipulando data e hora
python tem um modulo built in para se trabalhar com data e hora chamado datetime

'''
import datetime

#print(dir(datetime))

# Maior de ano
print(datetime.MAXYEAR)

# Menor
print(datetime.MINYEAR)

# Data atual
print(datetime.datetime.now())

inicio = datetime.datetime.now()
print(inicio)
# Mudando a hora
inicio = inicio.replace(hour=11,minute=0,second=0,microsecond=0)
print(inicio)

evento = datetime.datetime(2019,1,1,0)
print(type(evento))
print(evento)

aniversario = input("Informe a data de nascimento (dd/mm/yyyy): ")
print(aniversario)
nascimento = aniversario.split('/')
print(nascimento)
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]) , int(nascimento[0]))
print(nascimento)

print(inicio.day)
print(inicio.month)
print(inicio.year)
print(inicio.hour)
print(inicio.minute)
print(inicio.second)
print(inicio.microsecond)