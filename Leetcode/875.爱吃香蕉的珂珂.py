#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left,right=1,max(piles)
        while left<right:
            mid=(left+right)//2
            if sum([(pile + mid - 1) // mid for pile in piles]) > h:
                left=mid+1
            else:
                right=mid
        return left    
# @lc code=end
