from functools import reduce

nums = [5, 20, 3, 50, 2]

res = reduce(lambda x, y: x if x > y else y  , nums)
print(res)