#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups = defaultdict(list)
        def dfs(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return
            groups[col].append((row, node.val))  # col 相同的分到同一组
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)

        ans = []
        for _, g in sorted(groups.items()):
            g.sort()  # 按照 row 排序，row 相同按照 val 排序
            ans.append([val for _, val in g])
        return ans

# @lc code=end

