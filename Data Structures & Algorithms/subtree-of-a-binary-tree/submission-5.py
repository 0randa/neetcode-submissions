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

        sameSubFunc = False
        def dfs(root, subRoot) -> bool:
            nonlocal sameSubFunc
            if root is None or subRoot is None:
                print("grrr")
                return True

            # if the values are equal, check for a subtree.
            print(root.val, subRoot.val)

            if root.val == subRoot.val:
                sameSubFunc = sameTree(root, subRoot)
                print(sameSubFunc)

            return dfs(root.left, subRoot) and dfs(root.right, subRoot)

        ans = dfs(root,subRoot)

        if not sameSubFunc:
            print("hey")
            return False

        return ans