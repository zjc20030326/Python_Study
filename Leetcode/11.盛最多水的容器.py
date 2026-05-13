#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        n = len(height) - 1
        left = 0
        right = n
        while left < right:
            area = (right - left) * min(height[right], height[left])
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


# @lc code=end
