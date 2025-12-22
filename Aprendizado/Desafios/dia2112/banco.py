import sqlite3


def criacao():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
    CREATE TABLE filme (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        autor VARCHAR(50),
        genero VARCHAR(50),
        ano INT
    )
    """)
    
    conexao.commit()
    conexao.close()


def selecaoTotal():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM filme")
    res = cursor.fetchall()
    
    return res

def insercao(nome,autor,genero,ano):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    
    res = (nome,autor,genero,ano)
    cursor.execute("INSERT INTO filme(nome,autor,genero,ano) VALUES (?,?,?,?)",res)

    
    conexao.commit()
    conexao.close()
