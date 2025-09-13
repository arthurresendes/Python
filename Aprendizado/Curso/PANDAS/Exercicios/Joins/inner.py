import pandas as pd

clientes = pd.DataFrame({
    'Id': [1, 2, 3, 4],
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Cidade': ['SP', 'RJ', 'SP', 'MG']
})

pedidos = pd.DataFrame({
    'Id': [2, 3, 4, 5],
    'Produto': ['Notebook', 'Celular', 'Teclado', 'Mouse'],
    'Valor': [3500, 1800, 150, 50]
})

intersec = pd.merge(clientes,pedidos, on='Id', how="inner")
print(intersec)