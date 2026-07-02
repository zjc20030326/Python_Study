#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        return length

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.getLength(head)
        dummy = ListNode(next=head)
        p0 = dummy

        for _ in range(n // k):
            # p0 是当前这一组前面的节点
            # p0.next 是当前这一组的第一个节点，反转后会变成这一组的尾巴
            tail = p0.next

            pre = None
            cur = p0.next

            # 反转 k 个节点
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            # 接回链表
            p0.next = pre      # p0 接到反转后的头
            tail.next = cur    # 反转后的尾接到下一组

            # p0 移动到这一组的尾巴
            p0 = tail

        return dummy.next
# @lc code=end
