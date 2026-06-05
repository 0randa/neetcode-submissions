# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_ancest, max_ancest = root.val, root.val

        def dfs(node, min_ancest, max_ancest):
            if not node:
                return True

            min_ancest, max_ancest = min(node.val, min_ancest), max(node.val, max_ancest)
            print(node.val, min_ancest, max_ancest)

            # check that the left subtree is less than min ancestor
            if node.left:
                if node.left.val > min_ancest:
                    print("wow")
                    return False
            
            if node.right:
                if node.right.val < max_ancest:
                    print("haha")
                    return False

            return dfs(node.left, min_ancest, min_ancest) and dfs(node.right, min_ancest, max_ancest)

        return dfs(root, root.val, root.val)