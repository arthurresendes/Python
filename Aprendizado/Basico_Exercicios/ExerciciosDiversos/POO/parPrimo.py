import math

class Matematica:
    def __init__(self):
        pass
    
    @staticmethod
    def ehPar(n):
        if n % 2 == 0:
            return 'Par'
        else:
            return 'Impar'
    
    @staticmethod
    def primo(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

c = Matematica()

print(c.ehPar(22))
print(c.ehPar(21))

print(c.primo(17))
print(c.primo(53))
