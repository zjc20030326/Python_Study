#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def f(node, sum):
            nonlocal ans
            if node:
                sum = sum * 10 + node.val
            else:
                return
            if node.left is None and node.right is None:
                ans +=sum
                return
            f(node.left, sum)
            f(node.right, sum)
        f(root,0)
        return ans


# @lc code=end
