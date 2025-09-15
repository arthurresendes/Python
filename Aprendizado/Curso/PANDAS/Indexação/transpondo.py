import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods=6)

df = pd.DataFrame(np.random.randn(6,4) , index=datas, columns=['Var A', 'Var B', 'Var C', 'Var D'])

print(df.T) #Transpondo
print(df.shape) #Colunas e linhas
print(df.values)
print(df.value_counts())