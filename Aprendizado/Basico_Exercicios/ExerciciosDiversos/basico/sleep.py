import time

print("Contagem: ")
for i in range(9):
    print(9-i, end ='\r') #Sobrepoe o elemento
    time.sleep(1)
print("Fim")