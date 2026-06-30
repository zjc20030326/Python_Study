#
# @lc app=leetcode.cn id=2529 lang=python3
#
# [2529] 正整数和负整数的最大计数
#

# @lc code=start
class Solution:
    def lower_bound(self,nums:list[int],target:int)->int:
        left,right=0,len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
    def maximumCount(self, nums: list[int]) -> int:
        start=self.lower_bound(nums,0)
        end=self.lower_bound(nums,1)-1
        neg=start
        pos=len(nums)-1-end
        return max(neg,pos)
# @lc code=end

