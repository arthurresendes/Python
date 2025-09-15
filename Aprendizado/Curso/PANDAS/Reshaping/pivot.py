import pandas as pd
import numpy as np

dias = pd.date_range(start='20200101', periods=12)

pessoas = ['Arthur', 'Resende', 'Gomes']

np.random.choice(pessoas)

Nome = []
Gasto = []

for i in range(12):
    Nome.append(np.random.choice(pessoas))
    Gasto.append(np.random.rand()*100)


df = pd.DataFrame({'Dias': dias, 'Nome': Nome, 'Gasto':Gasto})

print(df.pivot(index='Dias',columns='Nome',values='Gasto'))