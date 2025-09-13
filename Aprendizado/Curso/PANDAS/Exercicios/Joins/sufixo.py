import pandas as pd

cadastro_a = pd.DataFrame({
    'Id': [101, 102, 103],
    'Nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 22]
})

cadastro_b = pd.DataFrame({
    'Id': [102, 103, 104],
    'Nome': ['Bob S.', 'Carlos M.', 'Diana'],
    'Idade': [31, 23, 28]
})

intersec = pd.merge(cadastro_a,cadastro_b, on='Id', how='inner', suffixes=('_A ','_B'))
print(intersec)
