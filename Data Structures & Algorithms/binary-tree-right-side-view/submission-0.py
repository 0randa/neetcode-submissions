# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        cur = root
        
        while cur:
            res.append(cur.val)
            cur = cur.right

        return res