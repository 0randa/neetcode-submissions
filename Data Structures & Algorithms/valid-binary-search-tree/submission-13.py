# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return True


            if root.left and not root.right:
                if root.val > root.left.val:
                    return True
                else:
                    return False

            elif not root.left and root.right:
                if root.val < root.right.val:
                    return True
                else:
                    return False

            elif root.left and root.right:
                if root.left.val < root.val < root.right.val:
                    return True
                else:
                    return False

            elif not root.left and not root.right:
                return True
            

            return dfs(root.left) and dfs(root.right)

        return dfs(root)