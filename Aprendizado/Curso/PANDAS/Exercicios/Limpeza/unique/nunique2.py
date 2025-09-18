import pandas as pd

df12 = pd.DataFrame({
    "Cidade": ["SP", "RJ", "SP", "BH", "BH", "RJ", "SP"]
})
print(df12.nunique())