import mysql.connector
# pip install mySql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "",
    password = "",
    database = "firma"
)

meu_cursor = conexao.cursor()

meu_cursor.execute("CREATE DATABASE firma")

for x in meu_cursor:
    print(x)