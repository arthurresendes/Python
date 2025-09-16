import pandas as pd
import numpy as np

datas = pd.date_range('20200101' , periods=600 , freq='D')
df = pd.DataFrame(np.random.randn(600,5) , index=datas , columns=list('ABCDE'))

print(df['D'].head(5))
print(df[1:5])
print(df.loc[:, ['B', 'C', 'D']])

print(df.loc['20200301': '20200901' , ['A', 'E']])