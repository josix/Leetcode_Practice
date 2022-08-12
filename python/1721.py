# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # setting two pointers to starting point
        terminal2 = ListNode(val=-1, next=head)
        terminal1 = ListNode(val=-1, next=terminal2)
        pointer_1_prev = terminal1
        pointer_1 = terminal2
        pointer_2_prev = terminal2
        pointer_2 = head
        for i in range(k - 1):
            pointer_2_prev = pointer_2_prev.next
            pointer_2 = pointer_2.next
        # keeping the begining of k node to be swapped
        swapping_node_1_prev = pointer_2_prev
        swapping_node_1 = pointer_2
        # traversing until pointer_2 is None, and we
        # will get the pos of the k node from the end that to be swapped
        while pointer_2 is not None:
            pointer_1 = pointer_1.next
            pointer_1_prev = pointer_1_prev.next
            pointer_2 = pointer_2.next
        swapping_node_2_prev = pointer_1_prev
        swapping_node_2 = pointer_1
        # print(f"case: \n{swapping_node_1=}\n{swapping_node_2=}\n{swapping_node_1_prev=}\n{swapping_node_2_prev=}")
        if swapping_node_1 is swapping_node_2: # case that swapping itself
            return head
        # case that swapping neighbors
        if swapping_node_2.next is swapping_node_1:
            swapping_node_1.next, swapping_node_2.next = swapping_node_2, swapping_node_1.next
            swapping_node_2_prev.next = swapping_node_1
            return terminal2.next # probably head has been moved
        if swapping_node_1.next is swapping_node_2:
            swapping_node_1.next, swapping_node_2.next = swapping_node_2.next, swapping_node_1
            swapping_node_1_prev.next = swapping_node_2
            return terminal2.next # probably head has been moved
        swapping_node_1.next, swapping_node_2.next =  swapping_node_2.next, swapping_node_1.next
        swapping_node_1_prev.next, swapping_node_2_prev.next = swapping_node_2, swapping_node_1
        return terminal2.next # since head has moved
