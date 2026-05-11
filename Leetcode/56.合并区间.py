#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        res = [[intervals[0][0], intervals[0][1]]]
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(intervals[i + 1][1], res[-1][1])]
            else:
                res.append(intervals[i + 1])
        return res


# @lc code=end
