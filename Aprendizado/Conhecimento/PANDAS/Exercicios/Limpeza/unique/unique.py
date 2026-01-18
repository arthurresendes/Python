import pandas as pd

df11 = pd.DataFrame({
    "Animal": ["Cachorro", "Gato", "Gato", "Cachorro", "Passarinho"],
    "Idade": [5, 3, 2, 5, 1]
})
print(df11.Animal.unique())