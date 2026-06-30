#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#
from bisect import bisect_left
# @lc code=start
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        left,right=0,len(citations)
        while left<right:
            mid=(left+right+1)//2
            if len(citations)-bisect_left(citations,mid)<mid:
                right=mid-1
            else:
                left=mid
        return left
# @lc code=end

