import numpy as np
import pandas as pd

vendas = pd.DataFrame({
    'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carla', 'Bruno', 'Ana'],
    'Produto': ['Notebook', 'Celular', 'Celular', 'Teclado', 'Teclado', 'Mouse'],
    'Valor': [3500, 1800, 2200, 150, 200, 50]
})

result = vendas.groupby(['Produto'])['Valor'].mean(numeric_only=True)
print(result)

