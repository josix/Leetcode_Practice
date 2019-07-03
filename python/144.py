# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack != []:
            item = stack.pop()
            ans.append(item.val)
            if item.right:
                stack.append(item.right)
            if item.left:
                stack.append(item.left)

        return ans
            
