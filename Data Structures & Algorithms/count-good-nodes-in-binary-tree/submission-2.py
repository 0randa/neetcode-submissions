# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # keep track of the maximum number

        
        bruh = 0

        def dfs(node, _max):
            nonlocal bruh
            if not node:
                return
            

            if node.val >= _max:
                bruh += 1

            # chuck in the maximum, traverse to the left



            dfs(node.left, max(_max, node.val))
            

            # undo that maximum, and then traverse to the right subtree

            dfs(node.right, node.val)

        dfs(root, root.val)

        return bruh

