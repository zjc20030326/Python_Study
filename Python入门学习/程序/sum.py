i = 0
sum = 0
while i <= 100**3:
    if i % 2 == 0:
        print(i, "是偶数！")
        sum += i
    i = i + 1
print("1000000以内所有偶数的和是", sum)
