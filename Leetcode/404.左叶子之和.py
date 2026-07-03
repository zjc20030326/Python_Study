#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def f(node):
            nonlocal ans

            if node is None:
                return

            # node.left 存在，并且它没有左右孩子，说明它是左叶子
            if (
                node.left is not None
                and node.left.left is None
                and node.left.right is None
            ):
                ans += node.left.val

            f(node.left)
            f(node.right)

        f(root)
        return ans


# @lc code=end
