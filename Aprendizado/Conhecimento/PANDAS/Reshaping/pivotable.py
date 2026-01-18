import pandas as pd
import numpy as np

dados = {
    'Loja': ['Loja A', 'Loja B', 'Loja A', 'Loja B', 'Loja A', 'Loja B'],
    'Produto': ['Produto 1', 'Produto 1', 'Produto 2', 'Produto 2', 'Produto 1', 'Produto 2'],
    'Vendas': [10, 20, 15, 25, 20, 30]
}

df = pd.DataFrame(dados)

print("DataFrame original:")
print(df)

# Criar a pivot table no Pandas
pivot_table = df.pivot_table(values='Vendas', index='Loja', columns='Produto', aggfunc='sum')

# Imprimir a pivot table no Pandas
print("\nPivot Table:")
print(pivot_table)