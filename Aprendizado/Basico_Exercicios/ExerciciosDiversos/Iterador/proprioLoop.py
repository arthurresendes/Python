import random

nums = []

for num in range(6):
    num = random.randint(1,100)
    nums.append(num)

num_ite = iter(nums)

while True:
    try:
        print(next(num_ite))
    except:
        break
print("Fim loop")