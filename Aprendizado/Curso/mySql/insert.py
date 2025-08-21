import mysql.connector
# pip install mySql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "",
    password = "",
    database = "firma"
)

meu_cursor = conexao.cursor()
nome = 'a'

ins = f"INSERT INTO tbcliente (nome, cpf) VALUES (%s, %s)" # -> Rever pq % s
valores = ('Arthur', '123-456-789-12')

meu_cursor.execute(ins,valores)

conexao.commit() # -> Rever

print(meu_cursor.rowcount, 'Inserido') # -> Rever