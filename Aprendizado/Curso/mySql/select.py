import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    username = "",
    password = "",
    database = "tbclientes"
)

meu_cursor = conexao.cursor()

meu_cursor.execute("SELECT * FROM tbclientes")

meu_result = meu_cursor.fetchall() # retorna uma lista de tuplas. Cada tupla contém os dados de uma linha da tabela. Se não houver mais linhas para retornar (por exemplo, a consulta retorna uma tabela vazia), fetchall() retornará uma lista vazia. Ou seja , faz retornar as linhas de uma consulta

for x in meu_result:
    print(x)