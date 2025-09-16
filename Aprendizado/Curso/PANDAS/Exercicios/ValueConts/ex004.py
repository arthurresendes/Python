'''
['Produto', 'Categoria']
'''

import pandas as pd

df = pd.DataFrame({
    'Produto': ['Cafe' , 'PC', 'Notebook', 'Geladeira'],
    'Categoria': ['Cultivo', 'Eletronico', 'Eletronico', 'Eletrodomestico']
})

valores = df.value_counts('Categoria')
print(valores)