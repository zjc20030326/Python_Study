#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if postorder == []:
            return 
        l=inorder.index(postorder[-1])
        left=self.buildTree(inorder[:l],postorder[:l])
        right=self.buildTree(inorder[l+1:],postorder[l:-1])
        return TreeNode(postorder[-1],left,right)
# @lc code=end

