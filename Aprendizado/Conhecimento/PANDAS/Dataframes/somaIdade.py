import pandas as pd

df = pd.read_excel("NomeCidadeIdade.xlsx")
soma_idade = df['Idade'].sum()
print(f"A soma das idades: {soma_idade}")