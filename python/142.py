# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        viewed_node = set()
        while head is not None and head not in viewed_node:
            viewed_node.add(head)
            head = head.next
        if head is None:
            return
        return head
