#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    def lower_bound(self,nums:list[int],target:int)->int:
        left,right=-1,len(nums)
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid
            else:
                right=mid
        return right
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans=0
        for i,x in enumerate(arr1):
            if self.lower_bound(arr2,x-d) <=(self.lower_bound(arr2,x+d+1)-1):
                continue
            else:
                ans+=1
        return ans
# @lc code=end

