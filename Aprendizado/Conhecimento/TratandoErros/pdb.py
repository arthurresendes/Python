'''
Debugando erros

Comando basicos pdb:

L -> Listar onde estamos no codigo

N -> Proxima linha

P -> Imprime variavel

C -> Continua a execução(finaliza debug)

Se quer ver uma variavel va para proxima linha da variavel e escreva o nome da variavel

Comando breakpoint utiliz os mesmo comandos para verificar

'''

import pdb

def dividir(a,b):
    breakpoint()
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f"Erro -> {err}")
print(dividir(4,7))

nome = 'Arthur'
sobrenome = 'Resende'
pdb.set_trace() # Ou import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python'
fim = nome_completo + ' faz curso de ' + curso
print(fim) 

def soma(a,b):
    breakpoint()
    return a + b

print(soma(1,2))