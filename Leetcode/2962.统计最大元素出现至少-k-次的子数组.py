#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans = 0
        left = 0
        cnt = 0
        m = max(nums)
        for right in range(len(nums)):
            if nums[right] == m:
                cnt += 1

            while cnt >= k:
                if nums[left] == m:
                    cnt -= 1
                left += 1
            ans += left
        return ans


# @lc code=end
