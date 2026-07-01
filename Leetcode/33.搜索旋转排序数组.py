#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                if target<=nums[-1]:
                    left=mid+1
                else:
                    if nums[mid]<=nums[-1]:
                        right=mid
                    else:
                        left=mid+1
            else:
                if target>nums[-1]:
                    right=mid
                else:
                    if nums[mid]>nums[-1]:
                        left=mid+1
                    else:
                        right=mid
        return -1 if nums[left]!=target else left
# @lc code=end

