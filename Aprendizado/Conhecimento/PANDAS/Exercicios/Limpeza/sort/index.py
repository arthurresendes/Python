import pandas as pd

df8 = pd.DataFrame({
    "Cidade": ["SP", "RJ", "BH", "POA"],
    "População": [12.3, 6.7, 2.5, 1.5]
}, index=[3, 1, 4, 2])
print(df8.sort_index())