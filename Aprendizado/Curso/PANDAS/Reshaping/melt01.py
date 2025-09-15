import pandas as pd

df = pd.DataFrame({
    'A':{0:'a',1:'b',2:'c'},
    'B':{0:1,1:3,2:5},
    'C':{0:2,1:4,2:6}
    
})

print(df)
melt = pd.melt(df,id_vars=['A'] , value_vars=['B'])
print(melt)
melt2 = pd.melt(df,id_vars=['A'] , value_vars=['B','C'], var_name="VarTeste" , value_name="Valores")
print(melt2)
