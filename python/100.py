# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        from collections import deque
        queue = deque([(p, q)])
        is_same = None
        while queue:
            node_p, node_q = queue.popleft()
            if node_p is None and node_q is None:
                is_same = True
            elif node_p is None or node_q is None:
                is_same = False
            elif node_p.val == node_q.val:
                is_same = True
            elif node_p.val != node_q.val:
                is_same = False
            
            if is_same and node_p is not None and node_q is not None:
                queue.append((node_p.left, node_q.left))
                queue.append((node_p.right, node_q.right))
            elif is_same and node_p is None and node_q is None:
                continue
            else:
                return False
        return True
        
