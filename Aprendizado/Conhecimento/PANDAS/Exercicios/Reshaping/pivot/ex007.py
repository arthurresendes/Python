'''
['Departamento', 'Funcionário', 'Salário']
'''

import pandas as pd

df = pd.DataFrame({
    'Departamento': ['Dados', 'TI', 'RH', 'Dados'],
    'Funcionario': ['Arthur', 'Jose', 'Amanda', 'Cacio'],
    'Salario': [2000,3000,4000,5000]
})

pivoTable = df.pivot_table(index='Funcionario', columns='Departamento' , values='Salario', aggfunc="mean")
print(pivoTable)