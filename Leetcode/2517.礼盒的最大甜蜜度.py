#
# @lc app=leetcode.cn id=2517 lang=python3
#
# [2517] 礼盒的最大甜蜜度
#

# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def f(d: int) -> int:
            cnt = 1
            pre = price[0]  # 先选一个价格最小的糖果
            for p in price:
                if p - pre >= d:  # 可以选 p
                    cnt += 1
                    pre = p
            return cnt

        price.sort()
        left = 0
        right = (price[-1] - price[0]) // (k - 1) + 1
        while left + 1 < right:  # 开区间不为空
            # 循环不变量：
            # f(left) >= k
            # f(right) < k
            mid = (left + right) // 2
            if f(mid) >= k:
                left = mid  # 下一轮二分 (mid, right)
            else:
                right = mid  # 下一轮二分 (left, mid)
        return left  # 最大的满足 f(left) >= k 的数
        
# @lc code=end

