import pandas as pd
import numpy as np
df2 = pd.DataFrame({
    "Produto": ["A", "B", "C", "D", "E"],
    "Preço": [10.5, np.nan, 8.0, np.nan, 12.0],
    "Quantidade": [5, 2, np.nan, 1, 3]
})


df2.dropna(inplace=True)
print(df2)