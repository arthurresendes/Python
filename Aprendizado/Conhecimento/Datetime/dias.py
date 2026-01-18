import datetime

hoje = datetime.datetime.today()
print(hoje)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)) , datetime.time())

print(manutencao)

'''
0 - Segunda
1 - Terça
2 - Quarta
3 - Quinta
4 - Sexta
5 - Sabado
6 - Domingo

'''

dia_semana = hoje.weekday()
if dia_semana == 0:
    print("Hoje é segunda")
elif dia_semana == 1:
    print("Hoje é Terça")
elif dia_semana == 2:
    print("Hoje é Qarta")
elif dia_semana == 3:
    print("Hoje é Quinta")
elif dia_semana == 4:
    print("Hoje é Sexta")
elif dia_semana == 5:
    print("Hoje é Sabado")
elif dia_semana == 6:
    print("Hoje é Domingo")
else:
    print('Erro')

def formata(data):
    if data.month == 1:
        return f"{data.day} no mês de Janeiro de {data.year}"
    elif data.month == 2:
        return f"{data.day} no mês de Fevereiro de {data.year}"
    elif data.month == 3:
        return f"{data.day} no mês de Março de {data.year}"
    elif data.month == 4:
        return f"{data.day} no mês de Abril de {data.year}"
    elif data.month == 5:
        return f"{data.day} no mês de Maio de {data.year}"
    elif data.month == 6:
        return f"{data.day} no mês de Junho de {data.year}"
    elif data.month == 7:
        return f"{data.day} no mês de Julho de {data.year}"
    elif data.month == 8:
        return f"{data.day} no mês de Agosto de {data.year}"
    elif data.month == 9:
        return f"{data.day} no mês de Setembro {data.year}"
    elif data.month == 10:
        return f"{data.day} no mês de Outubro {data.year}"
    elif data.month == 11:
        return f"{data.day} no mês de Novembro {data.year}"
    elif data.month == 12:
        return f"{data.day} no mês de Dezembro {data.year}"

print(formata(hoje))

nascimento  = input("Digite sua data de nascimento:  ")
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)


almoco = datetime.time(12,30,0)
print(almoco)