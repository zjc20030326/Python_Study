#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans


# @lc code=end
