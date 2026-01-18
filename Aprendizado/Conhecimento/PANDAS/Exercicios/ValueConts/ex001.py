import pandas as pd

def main():
    df = pd.DataFrame({
    'Nome': ['Jose', 'Amanda', 'Gabriel', 'Maria', 'Bruno', 'Ana', 'Lucas', 'Beatriz'],
    'Curso': ['Engenharia', 'Direito', 'Engenharia', 'Medicina', 'Direito', 'Engenharia', 'Medicina', 'Direito']
})
    aluno_curso = df.value_counts('Curso')
    print(aluno_curso)

if __name__ == "__main__":
    main()
