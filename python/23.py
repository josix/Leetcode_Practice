# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq as hq
        candidate = [(head.val, i, 0) for i, head in enumerate(lists) if head]
        if candidate == []:
            return None
        lists_length = []
        for head in lists:
            length = 0
            if head:
                current = head
                while current:
                    length += 1
                    current = current.next
            lists_length.append(length)
                
        hq.heapify(candidate)
        node = ListNode(None)
        head = node
        while True:
            node.val, list_index, sub_list_index = hq.heappop(candidate)
           
            if lists_length[list_index] - 1 != sub_list_index:
                next_candidate = lists[list_index]
                for _ in range(sub_list_index + 1):
                    next_candidate = next_candidate.next
                hq.heappush(candidate, (next_candidate.val ,list_index, sub_list_index + 1))
            if candidate != []:
                next_node = ListNode(None)
                node.next = next_node
                node = node.next
            else:
                break
            
        return head
            
            
