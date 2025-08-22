'''
Teste de memoria com generator

'''

def fib_lista(maximo):
    nums = []
    a,b = 0 , 1
    while len(nums) < maximo:
        nums.append(b)
        a,b = b , a + b
    return nums

for n in fib_lista(100):
    print(n)


def fib_gen(maximo2):
    a,b,contador = 0,1,0
    while contador < maximo2:
        a, b = b, a+b
        yield a
        contador += 1

fib = fib_gen(100)

for num in fib:
    print(num)