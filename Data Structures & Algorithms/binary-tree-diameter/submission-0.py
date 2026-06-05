# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # i think at every node, we should print the height of the 

        def height(root):
            if root is None:
                return 0

            lheight = height(root.left)
            rheight = height(root.right)
            
            Solution.diameter = max(Solution.diameter, lheight + rheight)

            return max(lheight, rheight) + 1
       

        height(root)
        return Solution.diameter

