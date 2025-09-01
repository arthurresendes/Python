'''
Getters e setters em Python

'''

class Conta:
    contador = 0

    def __init__(self, titular , saldo , limite):
        self.__id = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,novoLimite):
        self.__limite = novoLimite

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self,valor,conta):
        self.__saldo -= valor
        conta.__saldo += valor

conta1 = Conta('Arthur', 1000, 5000)
conta2 = Conta('Maria', 2000, 6000)

print(conta1.extrato())
print(conta2.extrato())
soma = conta1.saldo + conta2.saldo
print(soma)

