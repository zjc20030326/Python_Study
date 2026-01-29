import random
import timeit

haystack = [random.randint(1, 10000000) for i in range(10000000)]
needles = [random.randint(1, 1000) for i in range(1000)]

haystack = set(haystack)


def find():
    found = 0
    for each in needles:
        if each in haystack:
            found += 1

    print(f"一共找到{found}个匹配。")


t = timeit.timeit("find()", setup="from __main__ import find", number=1)
print(f"查找过程一共消耗{t}秒。")
