import pandas as pd

clientes = pd.DataFrame({
    'Id': [1, 2, 3, 4],
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel']
})

pedidos = pd.DataFrame({
    'Id': [1, 2, 2, 3, 4, 4],
    'Produto': ['Notebook', 'Celular', 'Mouse', 'Teclado', 'Cadeira', 'Mesa'],
    'Valor': [3500, 1800, 200, 150, 450, 600]
})

intersec = pd.merge(clientes,pedidos,on='Id',how='inner')

agrupando = intersec.groupby(['Nome'])['Valor'].sum(numeric_only=True)
print(agrupando)