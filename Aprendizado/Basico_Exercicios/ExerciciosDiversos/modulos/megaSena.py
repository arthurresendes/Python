import random

def mega_sena():
    print("----Mega Sena----")
    for i in range(6):
        num = random.randint(1,60)
        print(num, end = "| ")
mega_sena()
print("\n")