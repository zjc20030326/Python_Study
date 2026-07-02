#
# @lc app=leetcode.cn id=2487 lang=python3
#
# [2487] 从链表中移除节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        node = self.removeNodes(head.next)  # 返回的链表头一定是最大的
        if node.val > head.val:
            # 执行 head'.next = node 后，我们删除了从 head'（这里的 head' 是更前面的链表节点）到 node 之间的所有节点，包括当前的 head
            return node
        head.next = node
        return head
           
# @lc code=end

