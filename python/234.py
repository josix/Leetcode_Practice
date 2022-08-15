# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = ListNode(val=-1)
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = rev
            rev = slow
            slow = tmp
        if fast:
            slow = slow.next
        while slow and rev.val != -1:
            if rev.val != slow.val:
                return False
            slow = slow.next
            rev = rev.next
        return True

