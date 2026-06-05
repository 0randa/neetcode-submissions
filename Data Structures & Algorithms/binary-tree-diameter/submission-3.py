# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right:
            return 0


        def dfs(root):    
            if not root:
                return 1

            # sum of the left and right subtree
            return dfs(root.left) + dfs(root.right)

        return int(dfs(root) / 2)