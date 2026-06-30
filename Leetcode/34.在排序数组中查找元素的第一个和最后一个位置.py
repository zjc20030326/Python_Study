#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def lower_bound(self,nums:list[int],target:int)-> int:
        left,right=-1,len(nums)
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid
            else:
                right=mid
        return right
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self.lower_bound(nums, target)  # 选择其中一种写法即可
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]


# @lc code=end
