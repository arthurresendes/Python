import pandas as pd


df = pd.DataFrame({
        'Nome': ['Ana', 'João', 'Arthur', 'Mario'],
        'Idade': [20, 10, 75, 21],
        'Indexando':  [4,3,2,1]
})
df.set_index('Indexando', inplace=True)
print(df.sort_index())
print(df.sort_values('Idade'))
print(df.sort_values(by=['Nome', 'Idade']))
