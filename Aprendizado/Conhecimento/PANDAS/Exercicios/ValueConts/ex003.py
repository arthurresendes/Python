'''
['Cidade', 'Estado']
'''

import pandas as pd

df = pd.DataFrame({
    'Cidade': ['Osasco', 'SP', 'RJ', 'Salvador'],
    'Estado': ['São Paulo','São Paulo','Rio de JAneiro','Bahia']
})

valores = df.value_counts('Estado')
print(valores)