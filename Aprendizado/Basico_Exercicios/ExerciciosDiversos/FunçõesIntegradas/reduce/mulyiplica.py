from functools import reduce

nums = [1, 2, 3, 4, 5]

res = reduce(lambda x , y : x * y , nums)
print(res)