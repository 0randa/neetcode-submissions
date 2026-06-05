# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def sol(node):
            if not node:
                return

            # go to the right
            # if right exists, go right
            if node.right:
                res.append(node.val)
                sol(node.right)
            
            # if right doesn't exist, but left exists, go left
            elif not node.right and node.left:
                res.append(node.val)
                sol(node.left)

            # if neither exist, go right
            else:
                res.append(node.val)
                sol(node.right)


        sol(root)

        return res