"""
reverse -> So em lista

reversed -> Em tudo 
"""

for letra in reversed("Arthur Resende"):
    print(letra, end = "")

print("\n")
print("Arthur Resende"[::-1])

nome = 'Arthur Resende'
inverte = "".join(reversed(nome))
print(inverte)

for i in reversed(range(0,11)):
    print(i, end=" ")

print("\n")
for i in range(10,-1,-1):
    print(i, end=" ")