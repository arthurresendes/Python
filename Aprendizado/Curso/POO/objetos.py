'''
POO - Objetos

São instancias da class , ou seja pos o mapeamento do objeto do mundo real para sua representação computacional devemos criar quantos objetos forem necessarios , podemos pensar nos objetos/instancia 

'''

class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False
        
    def checar_lampada(self):
        return self.__ligada
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 4999
    
    def __init__(self,limite,saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

# Instancia / Objeto
lamp1 = Lampada('Branca', 110,60)

print(lamp1.checar_lampada())
lamp1.ligar_desligar()
print(lamp1.checar_lampada())