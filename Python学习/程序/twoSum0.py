import random

nums = []
i = 0
while i < 10000:
    nums.append(random.randint(1, 65535))
    i += 1
target = int(input("请录入目标整数:"))
n = len(nums)
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
