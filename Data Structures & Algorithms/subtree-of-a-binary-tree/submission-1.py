# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot) -> bool:
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False

            return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right))

        def dfs(root, subRoot) -> bool:
            if root is not None and subRoot is None:
                return False

            if root is None or subRoot is None:
                return True

            if root.val == subRoot.val:
                return sameTree(root, subRoot)

            return dfs(root.left, subRoot) and dfs(root.right, subRoot)

        return dfs(root, subRoot)