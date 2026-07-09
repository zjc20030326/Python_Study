#
# @lc app=leetcode.cn id=2476 lang=python3
#
# [2476] 二叉搜索树最近节点查询
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
        dfs(root)

        n = len(a)
        ans = []
        for q in queries:
            j = bisect_left(a, q)
            mx = a[j] if j < n else -1
            if j == n or a[j] != q:  # a[j]>q, a[j-1]<q
                j -= 1
            mn = a[j] if j >= 0 else -1
            ans.append([mn, mx])
        return ans
        
# @lc code=end

