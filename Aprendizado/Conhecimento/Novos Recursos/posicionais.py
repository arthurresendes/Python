'''
Argumentos somentes posicionais

'''

valor = '67.3'
# Convertendo valor para ponto flutuante
print(float(valor))


def cumprimentar(nome: str) -> str:
    return f"Olá {nome}"

print(cumprimentar("Arthur"))
print(cumprimentar(nome="Resende"))

def cumprimentar_v2(nome: str, /) -> str:
    return f"Ola {nome}"

print(cumprimentar_v2("Arthur"))
#print(cumprimentar_v2(nome='Arthur'))
# quando quiser que o valor seja passado sem o nome=... usa o / depois do parametro

def cumprimentar_v3(nome: str, /, mensagem: str = 'ola') -> str:
    return f"{mensagem} {nome}"

print(cumprimentar_v3("Arthur", mensagem='Bem-vindo'))

def cumprimentar_v4(*,nome: str) -> str:
    return f"Olá {nome}"

print(cumprimentar_v4(nome= "Arthur"))
# Para ter que passra o parametro obrigatoriamente usamos o * antes dos parametros

def cumprimentar_v5(nome: str, /, mensagem1: str = 'ola' , * , mensagem2 : str) -> str:
    return f"{mensagem1} {mensagem2} {nome}"

print(cumprimentar_v5("Arthur", mensagem1='Bem-vindo', mensagem2='a casa'))
print(cumprimentar_v5("Arthur", 'Bem-vindo', mensagem2='a casa'))
print(cumprimentar_v5("Arthur", mensagem2='prazer'))