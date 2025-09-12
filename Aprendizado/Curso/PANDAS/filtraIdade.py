import pandas as pd

df = pd.read_excel("NomeCidadeIdade.xlsx")
idade = df[df['Idade'] > 20]
print(idade)