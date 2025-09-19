import pandas as pd

df = pd.DataFrame({
    'Vendedor': ['Ana','Bruno','Carlos','Ana','Bruno','Carlos','Ana','Bruno','Carlos','Ana','Bruno','Carlos'],
    'Mês': ['Jan','Jan','Jan','Fev','Fev','Fev','Mar','Mar','Mar','Abr','Abr','Abr'],
    'Vendas': [1000,1200,1100,1500,1300,1200,2000,1800,1700,2100,1900,1600]
})

agrupaVend = df.groupby(['Vendedor'])['Vendas'].sum()
print(agrupaVend)
agrupaMes = df.groupby(['Mês'])['Vendas'].mean(numeric_only=True)
print(agrupaMes)