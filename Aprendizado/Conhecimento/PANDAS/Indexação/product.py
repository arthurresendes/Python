import pandas as pd

array = [0,1,2]
cor = ['red','green','blue','yellow']
print(pd.MultiIndex.from_product([array,cor] , names=('number','color')))