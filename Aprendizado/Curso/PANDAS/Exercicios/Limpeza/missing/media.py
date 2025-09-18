import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Daniel", "Eva"],
    "Idade": [23, np.nan, 30, np.nan, 27],
    "Cidade": ["SP", "RJ", np.nan, "BH", "SP"]
})
print(df1)


df1.Idade.fillna(value=df1['Idade'].mean() , inplace=True)
print(df1)