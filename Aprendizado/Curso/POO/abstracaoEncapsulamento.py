'''
POO - Abstração e encapsulamento


'''

class Conta:
    contador = 400
    
    def __init__(self,titular,saldo,limite):
        self.__id = Conta.contador +1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__id
    
    def extrato(self):
        print(f"Saldo de {self.__titular} , R$ {self.__saldo} de saldo e o limite é de {self.__limite}")
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor invalido")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Erro ao sacar')

conta1 = Conta("Arthur Resende" , 150.00, 1500.00)

print(conta1.__dict__)
conta1.sacar(100)
conta1.extrato()
conta1.depositar(1000)
conta1.extrato()