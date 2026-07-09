#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self,root,a):
        if root is None:
            return
        self.dfs(root.left,a)
        a.append(root.val)
        self.dfs(root.right,a)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=[]
        self.dfs(root,a)
        n=len(a)
        if n<k:
            return a[-1]
        return a[k-1]

# @lc code=end
