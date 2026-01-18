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
print(df[['Nome','Idade']])
print("\n")
df2 = pd.DataFrame(dados2)
adulto = df2[df2['Idade'] > 27]
print(adulto)
print(df.columns)
print(df.to_numpy())

df.to_excel("InformaçõesAlunos.xlsx", index=True)