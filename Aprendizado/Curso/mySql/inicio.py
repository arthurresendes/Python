import mysql.connector
# pip install mySql.connector

conexao = mysql.connector.connect(
    host = "",
    user = "",
    password = "",
    database = ""
)

meu_cursor = conexao.cursor()

meu_cursor.execute()