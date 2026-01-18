from random import choice

def saudacao(pessoa):
    def tipo():
        escolha = choice(("ola" , 'oi', 'eai'))
        return escolha
    return tipo() + " " + pessoa

print(saudacao('Arthur'))

def faz_rir(pessoa1):
    def rir():
        return choice(('hahahaha', 'kkkkkkkkkk', 'kakkakakakakkakkak'))
    return rir() + " " + pessoa1

rindo = faz_rir('Maria')

print(rindo)