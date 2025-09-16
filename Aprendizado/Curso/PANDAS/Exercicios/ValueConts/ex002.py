'''
['azul', 'vermelho', 'azul', 'verde', 'azul', 'vermelho']
'''

import pandas as pd

df = pd.DataFrame({
    'cores': ['azul', 'vermelho', 'azul', 'verde', 'azul', 'vermelho']
})

valores = df.value_counts('cores')
print(valores)