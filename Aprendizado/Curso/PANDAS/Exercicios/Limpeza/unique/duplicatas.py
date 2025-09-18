import pandas as pd

df15 = pd.DataFrame({
    "Aluno": ["Ana", "Bruno", "Ana", "Carlos", "Bruno", "Diana"],
    "Nota": [8, 7, 8, 9, 7, 10]
})
print("DataFrame original:")
print(df15)

pares_unicos = df15.drop_duplicates(subset=["Aluno", "Nota"])

print("\nPares únicos (Aluno, Nota):")
print(pares_unicos)