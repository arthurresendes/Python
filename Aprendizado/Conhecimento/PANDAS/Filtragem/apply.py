import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [1, 2, 3]})


pares = df.applymap(lambda x: 'Par' if x % 2 == 0 else 'Impar')
print(pares)
dois = df2.applymap(lambda x: x if x == 2 else "Não é 2")
print(dois)