import numpy as np
import pandas as pd


df = pd.DataFrame({
    "A": ['Verdadeiro','Falso','Verdadeiro','Falso','Verdadeiro','Falso','Verdadeiro','Falso'],
    "B":['um', 'um','dois','tres','dois','dois','um','tres'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})

print(df)
agrupamento = df.groupby(['A']).sum()
print(agrupamento)