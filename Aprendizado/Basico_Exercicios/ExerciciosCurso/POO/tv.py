class Televisao:
    def __init__(self, status , volume , canal):
        self.canal = canal
        self.volume = volume
        self.status = status

    def ligaDesliga(self,opcao):
        if opcao == 'Ligar':
            self.status = 'Ligado'
        elif opcao == 'Desligar':
            print("Desligando TV")
            self.status = 'Desligado'
            exit(1)
        else:
            print("Opção invalida")
        return self.status

    def vol(self , operador):
        if operador == "+":
            self.volume += 1
            print("Subindo de volume")
        elif operador == '-':
            self.volume -= 1
            print("Descendo de volume")
        else:
            print("Botão invalido")    
        return self.volume

    def can(self , operador2):
        if operador2 == "+":
            self.canal += 1
            print("Subindo de canal")
        elif operador2 == '-':
            self.canal -= 1
            print("Descendo de canal")
        elif isinstance(operador2,int):
            self.canal = operador2
        else:
            print("Botão invalido")    
        return self.canal

print("Bem vindo a ArTV")
statusLiga = input("Deseja ligar ou desligar TV(Ligar ou Desligar): ").title()
statusCanal = int(input("Qual canal quer assistir: "))
statusVol = int(input("Qual volume quer estar: "))
tv1 = Televisao(statusLiga, statusVol, statusCanal)

subirCanal = input("Deseja subir ou descer de canal (+ ou -): ")
if subirCanal == '+':
    print(f"Subindo {tv1.can('+')}")
elif subirCanal == '-':
    print(f"Subindo {tv1.can('-')}")
else:
    print("Opção invalida")