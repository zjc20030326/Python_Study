#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#


# @lc code=start
class Solution:
    def lower_bound(self, nums: list[int], target: int)-> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = self.lower_bound([x[0] for x in matrix], target)
        if m<len(matrix) and matrix[m][0]==target:
            return True
        else:
            if m==0:
                return False
            else:
                m-=1
                n = self.lower_bound(matrix[m], target)
                if n == len(matrix[0]):
                    return False
                else:
                    return  target == matrix[m][n]


# @lc code=end
