'''
['Loja', 'Categoria', 'Lucro']
'''

import pandas as pd

dados = pd.DataFrame({
    'Loja': ['Renner', 'C&A', 'Nike', 'Renner'],
    'Mes': [5,6,12,5],
    'Lucro': [9000,2000,7000,7000]
})

pivot = dados.pivot_table(index="Mes", columns='Loja', values="Lucro", aggfunc="sum")
print(pivot)