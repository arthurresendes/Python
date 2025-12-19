def ler_num() -> int:
    while True:
        try:
            a = int(input("Digite numero A: "))
            b = int(input("Digite numero B: "))
            c = int(input("Digite numero C: "))
            if isinstance(a,int) and isinstance(b,int) and isinstance(c,int):
                return a,b,c
        except:
            print("Erro, digite um numero valido!!")

def delta():
    a,b,c = ler_num()
    delta = b ** 2 - 4 * a * c
    return a,b,delta

def raiz():
    a,b,delt = delta()
    raiz = delt ** 0.5
    x1 = (-b + raiz)/ (2 * a)
    x2 = (-b - raiz)/ (2 * a)
    
    return x1,x2

if __name__ == "__main__":
    res1,res2 = raiz()
    print(f"Raiz 1: {res1}")
    print(f"Raiz 2: {res2}")