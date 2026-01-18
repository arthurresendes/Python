import pandas as pd
import matplotlib.pyplot as plt


df_linha = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [150, 200, 300, 250, 400, 350]
})

plt.figure(figsize=(8,4))
plt.plot(df_linha['Mês'] , df_linha['Vendas'], marker='o', linestyle='-', color='blue', label='Vendas')
plt.title("Vendas por Mês")      
plt.xlabel("Mês")                       
plt.ylabel("Vendas")                     
plt.grid(True, linestyle='--', alpha=0.5) 
plt.legend()                            
plt.show()