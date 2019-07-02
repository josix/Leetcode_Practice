# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        stack = []
        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if stack == []:
                return ans
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
