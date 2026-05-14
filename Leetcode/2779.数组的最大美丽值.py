#
# @lc app=leetcode.cn id=2779 lang=python3
#
# [2779] 数组的最大美丽值
#


# @lc code=start
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        n = len(nums)
        res = 0
        for right in range(n):
            while nums[left] + k < nums[right] - k:
                left += 1
            res = max(res, right - left + 1)
        return res


# @lc code=end
