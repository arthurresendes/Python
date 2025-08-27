def soma_args(func):
    def wrapper(*args,**kwargs):
        if isinstance(args[0], (int,float)):
            soma = sum(args)
            return soma
        else:
            print("Não sao numeros")
    return wrapper

@soma_args
def nums(*a):
    return a

print(nums(2,3,4,5,6,7))