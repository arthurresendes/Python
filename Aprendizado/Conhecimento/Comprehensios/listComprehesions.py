"""
Compreensão de lista: 

Podemos gerar novas listas com dados processados a partir de outro iteravel

Sintaxe:
[dado for dado in iteravel]
"""

num = [1,2,3,4,5]
# numero vezes 10 para cada numero na lista num
res = [numero * 10 for numero in num]

print(res)
"""
Entendendo melhor:
- for numero in num(for normal)
- Parte que o numero eh alterado
"""

newRes = [numero /2 for numero in num]
print(newRes)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in num]
print(res)


numerosDobrados = []
for numero in num:
    numero = numero * 2
    numerosDobrados.append(numero)

print(numerosDobrados)

print([numero * 2 for numero in num])
print([numero * 2 for numero in [2,4,6,8,10]])

nome = 'Arthur Resende'

print([letra.upper() for letra in nome])

def meusFriend(nome):
    nome = nome.replace(nome[0],nome[0].upper())
    return nome

listaAmigos = ['jose' , 'augusto', 'arthur', 'gabriel']

print([meusFriend(amigo) for amigo in listaAmigos])

print([number * 3 for number in range(1,11)])

print([str(numero) for numero in [1,2,3,4,5]])