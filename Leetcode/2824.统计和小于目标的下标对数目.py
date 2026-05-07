#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#


# @lc code=start
class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                res += right - left
                left += 1
            else:
                right -= 1
        return res


# @lc code=end
