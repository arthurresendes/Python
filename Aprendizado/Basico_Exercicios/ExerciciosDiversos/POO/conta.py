class Conta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor

    def exibir_saldo(self):
        print(f"Titular: {self.titular}\nSaldo: {self.saldo}")