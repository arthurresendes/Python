p = True  
q = False
r = True
Negq = not q
result = p and Negq == True
negResult = not result

if negResult or r == True:
    print(True)
else:
    print(False)

