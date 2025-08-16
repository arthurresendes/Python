num = int(input("Qual tabuada quer ver: "))
tabuada = 1
while tabuada != 11:
    if tabuada % 2 == 0:
        print(f"{num} x {tabuada} = {num * tabuada}")
    tabuada += 1