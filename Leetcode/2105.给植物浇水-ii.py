#
# @lc app=leetcode.cn id=2105 lang=python3
#
# [2105] 给植物浇水 II
#


# @lc code=start
class Solution:
    def minimumRefill(self, plants: list[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        left, right = 0, n - 1
        times = 0
        A = capacityA
        B = capacityB
        while left < right:
            if plants[left] <= A:
                A -= plants[left]
            else:
                A = capacityA - plants[left]
                times += 1
            left += 1
            if plants[right] <= B:
                B -= plants[right]
            else:
                B = capacityB - plants[right]
                times += 1
            right -= 1
        if n % 2 == 1 and A < plants[left] and B < plants[right]:
            times += 1
        return times


# @lc code=end
