#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans=0
        nums.sort()
        for i in range(len(nums)-1):
            ans += bisect_right(nums, upper - nums[i], i + 1, len(nums)) - bisect_left(
                nums, lower - nums[i], i + 1, len(nums)
            )
        return ans

# @lc code=end
