#
# @lc app=leetcode.cn id=2816 lang=python3
#
# [2816] 翻倍以链表形式表示的数字
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=self.reverseList(head)
        cur=dummy=ListNode()
        carry=0
        while p1 or carry:
            if p1: carry+=p1.val*2
            cur.next=ListNode(carry%10)
            carry//=10
            cur=cur.next
            if p1:
                p1=p1.next
        return self.reverseList(dummy.next)

# @lc code=end
