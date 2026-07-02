#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        right = dummy
        while right.next and right.next.next:
            val = right.next.val
            if val == right.next.next.val:
                while right.next and val == right.next.val:
                    right.next = right.next.next
            else:
                right = right.next
        return dummy.next


# @lc code=end
