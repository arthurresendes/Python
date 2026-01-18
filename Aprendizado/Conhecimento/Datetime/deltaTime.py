'''
data fim - data inicio

'''
import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2026,3,3,0)
tempo_paraEvento = aniversario - data_hoje
print(tempo_paraEvento)
print(f"Faltam {tempo_paraEvento.days} dias , {tempo_paraEvento.seconds // 60 // 60} horas")

data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
vencimento = data_compra + regra_boleto
print(vencimento)