#
# @lc app=leetcode.cn id=3217 lang=python3
#
# [3217] 从链表中移除在数组中存在的节点
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        remove_set = set(nums)

        dummy = ListNode(next=head)
        cur = dummy

        while cur.next:
            if cur.next.val in remove_set:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


# @lc code=end
