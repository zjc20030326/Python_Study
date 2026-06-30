#
# @lc app=leetcode.cn id=2439 lang=python3
#
# [2439] 最小化数组中的最大值
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(limit: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                new_num = nums[i] + extra  # 把多出的积木堆到 nums[i] 上
                extra = max(new_num - limit, 0)  # 如果 new_num - limit > 0，那么多出的积木继续丢给左边
            return nums[0] + extra <= limit

        return bisect_left(range(max(nums)), True, lo=nums[0], key=check)

# @lc code=end

