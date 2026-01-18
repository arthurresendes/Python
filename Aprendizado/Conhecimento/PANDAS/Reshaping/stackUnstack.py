import pandas as pd


df = pd.read_excel("table.xlsx" , sheet_name='Planilha1')
print(df.shape)
stack_df = df.stack()
print(stack_df)
unstack_df = df.unstack()
print(unstack_df)
