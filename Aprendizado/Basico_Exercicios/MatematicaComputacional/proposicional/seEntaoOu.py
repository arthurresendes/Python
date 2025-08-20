p =  True
q = False
r = True
result1 = None
result2 = None


if p == True and q == False:
    result1 = False
else:
    result1 = True
    
if not q == True and r == False:
    result2 = False
else:
    result2 = True

if result1 or result2 == True:
    print(True)
else:
    print(False)