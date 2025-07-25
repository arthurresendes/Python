"""
**kwargs

Ordem nas funções:

-Parametros obriatorios
- *args
- Paremtros default
- **kwargs

"""
def cores(**dados):
    return dados

print(cores(Arthur = 'Azul' , Isac = 'Vermelho' , Pedro = 'Preto'))

"""Função de cumprimento:
    se a chave for nome no dicionario e a chave nome for igual a Arthur
    se nao se nome tiver no kwargs retorna outra coisa
    se nao retorna não sabe quem eh
    """
def cumprimento_especial(**kwargs):
    if 'nome' in kwargs and kwargs['nome'] == 'Arthur':
        return "Você eh de mais"
    elif 'nome' in kwargs:
        return f"{kwargs['nome']} Arthur!"
    return "Não sei quem você eh"


print(cumprimento_especial())
print(cumprimento_especial(nome = 'Arthur'))
print(cumprimento_especial(nome = 'oi'))
print(cumprimento_especial(nome ='especial'))

print("\n")

def minha_funcao(idade , nome , *args , solteiro = False ,**kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro == False:
        print('Casado')
    else:
        print("Solteiro")
    print(kwargs)

minha_funcao(18, 'Arthur')
minha_funcao(18, 'Josef' , 4,5,4, solteiro = True, eleEh = 'Phyton')

def mostra_info(a,b,*args,instrtutor = 'Skibi' , **kwargs):
    return [a,b,*args,instrtutor,kwargs]

print(mostra_info(3,4,3,sobrenome = 'Bidi' , instrtutor = 'Sim' , nome = 'Josef'))