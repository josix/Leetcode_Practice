# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = slow = fast = ListNode(-1, next=head)
        fast = fast.next
        while fast and fast.next:
            meet_duplicated = False
            # print(f"before {slow.val=}, {fast.val=}")
            while fast.val == fast.next.val:
                fast.next = fast.next.next
                meet_duplicated = True
                if fast.next is None:
                    break
            if meet_duplicated:
                # print(f"{fast=}{slow=}")
                fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
                fast = fast.next
                # print(f"after {slow.val=}, {fast.val=}")
        return dummy.next
