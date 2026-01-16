import random

counts = int(input("请输入抛硬币的次数："))
heads = 0  # 正面次数
tails = 0  # 反面次数
current_heads = 0  # 当前连续正面次数
current_tails = 0  # 当前连续反面次数
max_heads = 0  # 最多连续正面次数
max_tails = 0  # 最多连续反面次数

print("开始抛硬币实验......")
for i in range(counts):
    num = random.randint(0, 1)

    if num == 1:  # 正面
        heads += 1
        current_heads += 1
        # 反面连续中断,更新最大值并重置
        if current_tails > max_tails:
            max_tails = current_tails
        current_tails = 0

        if counts <= 100:
            print("正面", end=" ")
    else:  # 反面
        tails += 1
        current_tails += 1
        # 正面连续中断,更新最大值并重置
        if current_heads > max_heads:
            max_heads = current_heads
        current_heads = 0

        if counts <= 100:
            print("反面", end=" ")

# 循环结束后,检查最后一段连续
if current_heads > max_heads:
    max_heads = current_heads
if current_tails > max_tails:
    max_tails = current_tails

print("\n一共模拟了", counts, "次抛硬币,结果如下:")
print("正面:", heads, "次")
print("反面:", tails, "次")
print("最多连续正面:", max_heads, "次")
print("最多连续反面:", max_tails, "次")
