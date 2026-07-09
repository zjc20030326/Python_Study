#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(postorder)}
        def dfs(pre_l: int, pre_r: int, post_l: int) -> Optional[TreeNode]:
            if pre_l==pre_r:
                return
            if pre_l+1==pre_r:
                return TreeNode(preorder[pre_l])
            l=index[preorder[pre_l+1]]-post_l+1
            left=dfs(pre_l+1,pre_l+l+1,post_l)
            right=dfs(pre_l+l+1,pre_r,post_l+l)
            return TreeNode(preorder[pre_l],left,right)
        return dfs(0,len(preorder),0)
# @lc code=end

