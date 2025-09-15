import pandas as pd

def main():
    df = pd.DataFrame({
    'Aluno': ['Jose','Amanda','Jose','Amanda'],
    'Materia': ['Mat','Mat','Mat','Mat'],
    'Nota': [9,3,5,6]
    })
    pivot = df.pivot_table(index='Aluno', columns='Materia' , values='Nota',aggfunc='mean')
    print(pivot)

if __name__ == "__main__":
    main()