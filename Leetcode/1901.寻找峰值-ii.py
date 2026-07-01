#
# @lc app=leetcode.cn id=1901 lang=python3
#
# [1901] 寻找峰值 II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat) - 2
        while left <= right:
            i = (left + right) // 2
            mx = max(mat[i])
            if mx > mat[i + 1][mat[i].index(mx)]:
                right = i - 1  # 峰顶行号 <= i
            else:
                left = i + 1  # 峰顶行号 > i
        return [left, mat[left].index(max(mat[left]))]
        
# @lc code=end

