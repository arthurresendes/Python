import pandas as pd

data = {
    "localizacao": ['CidadeA', 'CidadeB'],
    "Temperatura": ['Prevista', 'Atual'],
    'Set-2019': [30,22],
    'Out-2019': [45,43],
    'Nov-2019': [24,22]
}

df = pd.DataFrame(data , columns=['localizacao','Temperatura', 'Set-2019', 'Out-2019','Nov-2019'])
print(df)

df2 = pd.melt(df , id_vars=['localizacao','Temperatura'], value_vars=['Set-2019', 'Out-2019','Nov-2019'], var_name='Data', value_name="Valor")
print(df2)

print("\n\n\n\n")
print(df2.loc[1, ['localizacao', 'Temperatura', 'Valor']])
