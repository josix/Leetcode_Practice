# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if not fast:
            return
        fast = fast.next
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                fast = fast.next
            else:
                slow.next = fast.next
                fast = fast.next
        return head
