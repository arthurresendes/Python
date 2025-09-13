import pandas as pd
dados = [
    {'Nome': 'Ana', 'Idade': 25, 'Cidade': 'São Paulo'},
    {'Nome': 'Bruno', 'Idade': 30, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Carla', 'Idade': 28, 'Cidade': 'Belo Horizonte'}
]

dados2 = {'Nome': ['Ana', 'Bruno','Carla'],
        'Idade': [25,30,28],
        'Cidade': ['São Paulo', 'Belo Horizonte', 'Rio de Janeiro']
        }
df = pd.DataFrame(dados)
df2 = pd.DataFrame(dados2)
concatena = pd.concat([df,df2])
print(concatena)