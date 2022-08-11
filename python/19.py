class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        kept_head = head
        terminal_node = ListNode(val=-1, next=head)
        pointer_1 = terminal_node
        pointer_2 = head
        for i in range(n-1):
            pointer_2 = pointer_2.next
        # print(f"Init {pointer_1=} {pointer_2=}")
        while pointer_2.next != None:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next
        # print(f"Traverse {pointer_1=} {pointer_2=}")
        if pointer_1 is terminal_node:
            return head.next
        else:
            pointer_1.next = pointer_1.next.next
        return kept_head
