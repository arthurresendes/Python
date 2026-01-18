import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "",
    password = "",
    database = "tbcliente"
)

meu_cursor = conexao.cursor()

ins = "INSERT INTO tbcliente (nome, cpf) VALUES (%s, %s)"
val = [
    ('Arthur', '123-456-789-12'),
    ('Arthur', '124-456-789-12'),
    ('Arthur', '125-456-789-12'),
    ('Arthur', '126-456-789-12'),
]


meu_cursor.execute(ins,val)

conexao.commit()

print(meu_cursor.rowcount, 'inserido')