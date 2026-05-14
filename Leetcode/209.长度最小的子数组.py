#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        s = 0
        n = len(nums)
        ans = n + 1
        for right, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0


# @lc code=end
