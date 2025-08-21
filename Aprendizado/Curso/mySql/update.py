import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    username = "",
    password = "",
    database = "tbclientes"
)

meu_cursor = conexao.cursor()

sql = "UPDATE tbcliente SET nome = 'Rodrigo' WHERE id = 1"
meu_cursor.execute(sql)

conexao.commit() # Confirma a transação

print(meu_cursor.rowcount, 'Inserido') # Quantas linhas afetadas