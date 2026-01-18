'''
Iterador - Um objeto que pode ser iterado. Um objeto que retorna um elemento por vez quandon a função next é chamada

Iteravel - Um objeto que irá retornar um iterador , quando a função iter for chamada
'''

nome = 'Geek' # -> é um iteravel , não um iterador
numero = [1,2,3,4,5,6]  # -> é um iteravel , não um iterador

# Transformamos em um iterador
it1 = iter(nome)
it2 = iter(numero)

# Mostramos ele se iterando, so conseguimos usar o next se a variavel for iterador
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


nome2 = 'Arthur'
# Por tras no python faz o nome2 virar iterador por meio do iter e no print 'usa' o next.
for letra in nome2:
    print(letra)