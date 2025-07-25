def aniversario(dia,mes,ano):
    juntaTudo = "/".join([dia,mes,ano])
    if mes == "1":
        return f"Você nasceu dia {dia} em Janeiro de {ano}"
    elif mes == "2":
        return f"Você nasceu dia {dia} em Fevereiro de {ano}"
    elif mes == "3":
        return f"Você nasceu dia {dia} em Março de {ano}"
    elif mes == "4":
        return f"Você nasceu dia {dia} em Abril de {ano}"
    elif mes == "5":
        return f"Você nasceu dia {dia} em Maio de {ano}"
    elif mes == "6":
        return f"Você nasceu dia {dia} em Junho de {ano}"
    elif mes == "7":
        return f"Você nasceu dia {dia} em Julho de {ano}"
    elif mes == "8":
        return f"Você nasceu dia {dia} em Agosto de {ano}"
    elif mes == "9":
        return f"Você nasceu dia {dia} em Setembro de {ano}"
    elif mes == "10":
        return f"Você nasceu dia {dia} em Outubro de {ano}"
    elif mes == "11":
        return f"Você nasceu dia {dia} em Novembro de {ano}"
    elif mes == "12":
        return f"Você nasceu dia {dia} em Dezembro de {ano}"
    else:
        return "Mês inválido"
    

day = input("Digite o dia do seu aniversario: ")
month =  input("Digite o mês do seu aniversario: ")
year = input("Digite o ano do seu nascimento: ")

print(aniversario(day,month,year))