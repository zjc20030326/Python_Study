#
# @lc app=leetcode.cn id=2958 lang=python3
#
# [2958] 最多 K 个重复元素的最长子数组
#


# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        ans = 0
        cnt = Counter()  # type: ignore
        left = 0
        for right, c in enumerate(nums):
            cnt[c] += 1
            while cnt[c] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
