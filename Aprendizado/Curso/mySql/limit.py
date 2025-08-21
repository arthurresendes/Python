import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    username = "",
    password = "",
    database = "tbclientes"
)

meu_cursor = conexao.cursor()

meu_cursor.execute("SELECT * FROM tbclientes LIMIT 5")

meu_result = meu_cursor.fetchall() 

for x in meu_result:
    print(x)