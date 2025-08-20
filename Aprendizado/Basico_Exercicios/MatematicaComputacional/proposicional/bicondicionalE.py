p = True  
q = False
r = True
result1 = None
result2 = None

if p or q == True:
    result1 = True
else:
    result1 = False

if not p == True and r == False:
    result2 = False
else:
    result2 = True

if result1 == result2:
    print(True)
else:
    print(False)