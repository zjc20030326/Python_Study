#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#


# @lc code=start
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
#         while left + 1 < right:  # 开区间不为空
#             mid = (left + right) // 2
#             if nums[mid] < nums[-1]:
#                 right = mid
#             else:
#                 left = mid
#         return nums[right]

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
#         while left + 1 < right:  # 开区间不为空
#             mid = (left + right) // 2
#             if nums[mid] == nums[right]:
#                 right -= 1
#             elif nums[mid] < nums[right]:
#                 right = mid
#             else:
#                 left = mid
#         return nums[right]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 2
        while left <= right and nums[left] == nums[-1]:
            left += 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]


# @lc code=end
