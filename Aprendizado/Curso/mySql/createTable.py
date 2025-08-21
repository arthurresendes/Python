import mysql.connector
# pip install mySql.connector

conexao = mysql.connector.connect(
    host = "",
    user = "",
    password = "",
    database = "tbcliente"
)

meu_cursor = conexao.cursor()

meu_cursor.execute("CREATE table tbcliente (ID int auto_increment PRIMARY KEY ,nome VARCHAR(200), cpf UNIQUE VARCHAR(15))")

for x in meu_cursor:
    print(x)