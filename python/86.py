# https://leetcode.com/problems/partition-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return 
        left_head = left = ListNode(-1)
        right_head = right = ListNode(-1)
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        if right.next:
            right.next = None
        left.next = right_head.next
        return left_head.next
        


