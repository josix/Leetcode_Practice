# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        visited_1 = []
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            visited_1.append(slow.val)
            slow = slow.next

        visited_2 = []
        while slow:
            visited_2.append(slow.val)
            slow = slow.next
            
        if len(visited_1) < len(visited_2):
            visited_2.pop(0)
        

        for i in range(len(visited_1)):
            if visited_1[i] != visited_2[len(visited_2) - i - 1]:
                return False
        return True

