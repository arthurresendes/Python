import pandas as pd
import numpy as np

dates = pd.date_range('20200101' , periods=60, freq='D')
df = pd.DataFrame(np.random.randn(60,5) , index=dates , columns=list("ABCDE"))
print(df)

df['F'] = df.A[df.A > 0]
print(df.head(5))

df2 = df.copy()
df3 = df.copy()

df2.dropna().shape
print(df2.head(5))
df3.F.fillna(np.mean(df3.A), inplace=True)
print(df3.head(5))
df4 = df.copy()
df4.fillna(value=777 , inplace=True)
print(df4.head(5))
'''
inplace - modoifica diretamente
dropna - apaga registros que tem nan
fillna substitui valores
'''
