class ContaBancaria:
    def __init__(self , titular: str, saldo : float):
        self.titular = titular
        self.saldo = saldo
    
    def apresentar(self):
        return f"Essa é a conta bancaria da pessoa {self.titular} com o saldo de {self.saldo}"

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular: str, saldo: float):
        super().__init__(titular,saldo)
    
    def apresentar(self):
        return f"Essa é a conta bancaria da pessoa {self.titular} com o saldo de {self.saldo * 1.05}"

p1 = ContaBancaria('Arthur', 2000.00)
print(p1.apresentar())
p2 = ContaPoupanca('Jose', 2000.00)
print(p2.apresentar())