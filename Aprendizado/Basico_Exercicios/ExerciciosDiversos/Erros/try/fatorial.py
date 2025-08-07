f = 1 
num = None
while True:
    try:
        num = int(input("Digite um num: "))
    except ValueError:
        print("Digite um numero!!")
    else:
        break
for n in range(1,num + 1):
    f = f * n 
print(f)