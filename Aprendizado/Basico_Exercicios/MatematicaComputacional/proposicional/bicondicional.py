p = True  
q = False
r = True
resultBi1 = None
result2 = None

if p == q:
    resultBi1 = True
else:
    resultBi1 = False

if q or r == True:
    result2 = True
else:
    result2 = False

if resultBi1 == True and result2 == False:
    print(True)
else:
    print(False)
