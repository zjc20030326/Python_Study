#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#

# @lc code=start
class Solution:
    def lower_bound(self,spell:int,nums:list[int],target:int)->int:
        left,right=0,len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]*spell<target:
                left=mid+1
            else:
                right=mid
        return left
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        ans=[]
        for i in range(len(spells)):
            ans.append(len(potions)-self.lower_bound(spells[i],potions,success))
        return ans
            
# @lc code=end

