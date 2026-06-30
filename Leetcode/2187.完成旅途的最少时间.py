#
# @lc app=leetcode.cn id=2187 lang=python3
#
# [2187] 完成旅途的最少时间
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, totalTrips*min(time)
        while left<right:
            mid=(left+right)//2
            if sum([mid//x for x in time])<totalTrips:
                left=mid+1
            else:
                right=mid
        return left
# @lc code=end
