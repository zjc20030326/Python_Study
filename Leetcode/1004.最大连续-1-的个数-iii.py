#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#


# @lc code=start
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = 0
        left = 0
        cnt = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# @lc code=end
