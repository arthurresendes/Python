import pandas as pd
import numpy as np

df4 = pd.DataFrame({
    "Cidade": ["SP", "RJ", "SP", "BH", "BH"],
    "População": [12.3, np.nan, np.nan, 2.5, 2.7]
})


df4.fillna(value=0, inplace=True)
print(df4)
