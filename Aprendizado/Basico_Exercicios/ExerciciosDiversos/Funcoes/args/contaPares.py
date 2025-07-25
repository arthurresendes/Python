def conta_pares(*numbers):
    total = 0
    for num1 in numbers:
        if num1 % 2 == 0:
            total += 1
    return total

print(conta_pares(1,2,3,4,5,6,7,8,9))