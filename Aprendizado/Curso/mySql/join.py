import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    username = "",
    password = "",
    database = "tbclientes"
)

meu_cursor = conexao.cursor()

sql = "SELECT \
  users.nome AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

meu_cursor.execute(sql)

meu_result = meu_cursor.fetchall() 

for x in meu_result:
    print(x)