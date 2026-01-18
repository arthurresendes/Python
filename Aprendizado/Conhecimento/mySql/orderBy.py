import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    username = "",
    password = "",
    database = "tbclientes"
)

meu_cursor = conexao.cursor()

sql = "SELECT * FROM tbclientes ORDER BY nome "
meu_cursor.execute(sql)

meu_result = meu_cursor.fetchall() 

for x in meu_result:
    print(x)