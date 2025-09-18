import pandas as pd

dados = {'Produto': ['Maçã', 'Banana', 'Maçã', 'Laranja', 'Banana', 'Maçã'],
    'Preço': [1.0, 0.5, 1.0, 0.8, 0.5, 1.1]}
df = pd.DataFrame(dados)

print("DataFrame original:")
print(df)
print(df.nunique())
print("\n")

df2 = df.copy()

print(df2.nunique(axis=1 , dropna=False))

df3 = df.drop_duplicates()
print(df3)

produtos_unicos = df['Produto'].unique()
print("Valores únicos na coluna 'Produto':")
print(produtos_unicos)