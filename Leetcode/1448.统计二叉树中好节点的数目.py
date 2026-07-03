#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def f(node, path_max):
            nonlocal ans

            if node is None:
                return

            # 判断当前节点是不是好节点
            if node.val >= path_max:
                ans += 1

            # 更新根节点到当前节点路径上的最大值
            path_max = max(path_max, node.val)

            # 无论孩子是不是好节点，都必须继续递归
            f(node.left, path_max)
            f(node.right, path_max)

        f(root, root.val)
        return ans


# @lc code=end
