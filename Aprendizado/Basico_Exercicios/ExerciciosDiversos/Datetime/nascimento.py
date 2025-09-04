import datetime

nascimento = datetime.datetime(2006,12,1)
dia_atual = datetime.datetime.now()
idade = dia_atual - nascimento
anos = idade.days // 365
print(f"Você tem {anos} anos com {idade.days} dias")