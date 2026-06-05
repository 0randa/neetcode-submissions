# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # i think at every node, we should print the height of the 
        diameter = 0

        def height(root):
            nonlocal diameter
            if root is None:
                return 0

            lheight = height(root.left)
            rheight = height(root.right)
            
            diameter = max(diameter, lheight + rheight)

            return max(lheight, rheight) + 1
       

        height(root)
        return diameter

