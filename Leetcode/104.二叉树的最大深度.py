#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        def f(node,cnt):
            if node is None:
                return
            cnt+=1
            nonlocal ans
            ans=max(ans,cnt)
            
            f(node.left,cnt)
            f(node.right,cnt)
        f(root,0)
        return ans
# @lc code=end
