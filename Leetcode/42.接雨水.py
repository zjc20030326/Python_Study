#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        suf_max = [0] * n
        pre_max[0] = height[0]
        suf_max[-1] = height[-1]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
            suf_max[n - i - 1] = max(suf_max[n - i], height[n - i - 1])
        ans = 0
        for j in range(0, n):
            ans += min(pre_max[j], suf_max[j]) - height[j]
        return ans


# @lc code=end
