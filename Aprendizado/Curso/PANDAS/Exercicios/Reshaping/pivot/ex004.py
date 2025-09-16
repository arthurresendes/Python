'''
['Loja', 'Categoria', 'Lucro']
'''

import pandas as pd

dados = pd.DataFrame({
    'Loja': ['Renner', 'C&A', 'Nike', 'Adidas'],
    'Categoria': ['A','B','A','A'],
    'Lucro': [9000,2000,7000,7000]
})

pivot = dados.pivot(index="Categoria", columns='Loja', values="Lucro")
print(pivot)