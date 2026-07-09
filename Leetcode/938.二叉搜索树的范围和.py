#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def f(node):
            nonlocal ans
            if node is None:
                return
            if low<=node.val<=high:
                ans+=node.val
            f(node.left)
            f(node.right)
        f(root)
        return ans
# @lc code=end

