p = True
q = False
r = True
result = p or q == True
negResult = not result
if negResult == True and r == False:
    print(False)
else:
    print(True)