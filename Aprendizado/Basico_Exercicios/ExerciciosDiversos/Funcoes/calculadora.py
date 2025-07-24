def soma(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def divi(a,b):
    return a / b

def mat(a,b,operacao=soma):
    return operacao(a,b)

print(mat(5,5,sub))
print(mat(5,5,multi))
print(mat(5,5,divi))
print(mat(5,5))