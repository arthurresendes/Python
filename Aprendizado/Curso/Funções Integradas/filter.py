"""
Filter
"""
import statistics

dados = [1.3,2.7,0.8,4.1,4.3,-0.1,2.7]

media = statistics.mean(dados)
mediana = statistics.median(dados)
moda = statistics.mode(dados)

print(media)
print(mediana)
print(moda)

res = list(filter(lambda x: x > media and x > mediana , dados))
print(res)

paises = ['', 'Argentina', 'Brasil', ' ', 'Paraguai', 'Chile' , ' ']
res1 = list(filter(lambda pais: pais not in ' ', paises))

# Ou: res1 = list(filter(None, paises)) , list(filter(lambda x: len(x) > 0, paises))
print(res1)

user = [
    {'username': 'Samuel', 'Tweets': ['Eu adoro bolos' , 'Eu adoro Pizza']},
    {'username': 'Carla', 'Tweets': ['Eu adoro gatos']},
    {'username': 'Jeff', 'Tweets': []},
    {'username': 'bob123', 'Tweets': []},
    {'username': 'doggo', 'Tweets': ['Vou sair hoje' , 'Eu adoro cachorros']},
    {'username': 'gal', 'Tweets': []}
]


# res2 = list(filter(lambda u: len(u['Tweets']) == 0  , user))
res2 = list(filter(lambda u: not u['Tweets'] , user))
res3 = list(filter(lambda u: u['username'] == 'doggo'  , user))
print(res2)
print("\n")
print(res3)

nomes = ['Vanessa', 'Ana', 'Maria']
res4 = list(map(lambda name: f"Sua instrutora é {name}" ,filter(lambda qtd: len(qtd) >= 5, nomes)))
print(res4)