import pandas as pd

dados = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(dados, index=['a', 'b', 'c'])
print(df)

novo_indice = ['b', 'a', 'd', 'c']
df_reindexado = df.reindex(novo_indice)
print(df_reindexado)