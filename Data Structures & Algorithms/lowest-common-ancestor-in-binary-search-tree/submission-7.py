# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        
        def dfs(root):
            if not root:
                return null

            # if they're both in different trees, return root, or if both p and q are in the right subtree
            if ((p.val < root.val < q.val or q.val < root.val < p.val) or (q.val > root.val and p.val >= root.val) or
            (root.val == p.val or root.val == q.val)):
                return root

            # both less than, traverse to the left
            elif (p.val < root.val) and (q.val < root.val):
                return dfs(root.left)
            
        return dfs(root)