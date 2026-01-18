import pandas as pd
import numpy as np

datas = pd.date_range('20200101' , periods=600 , freq='D')
df = pd.DataFrame(np.random.randn(600,5) , index=datas , columns=list('ABCDE'))

print(df.C)

print(df.A > 0)
print(df > 0)
print((df.A > 0) & (df.B > 0))