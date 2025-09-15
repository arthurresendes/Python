import pandas as pd

arrays = [[1,1,2,2] , ['red','blue','red','blue']]
print(pd.MultiIndex.from_arrays(arrays , names=('number','color')))