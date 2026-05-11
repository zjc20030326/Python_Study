#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#


# @lc code=start
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res


# @lc code=end
