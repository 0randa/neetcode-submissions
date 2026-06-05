# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_ancest, max_ancest = root.val, root.val

        # def dfs(node, min_ancest, max_ancest):
        #     if not node:
        #         return True

        #     smallest_acc_left, smallest_acc_right = min_ancest
        #     largest_acc_left, largest_acc_right = max_ancest

        #     # check that the left subtree is less than min ancestor
        #     if node.left:
                
        #         # the largest acceptable value will be 

        #         if node.left.val >= min_ancest:
        #             print("wow")
        #             return False
            
        #     if node.right:
        #         if node.right.val <= max_ancest:
        #             print("haha")
        #             return False

        #     return dfs(node.left, min_ancest, min_ancest) and dfs(node.right, min_ancest, max_ancest)

        def dfs(node, min_ancestor, max_ancestor):
            if not node:
                return True

            min_ancestor, max_ancestor = min(node.val, min_ancestor), max(node.val, max_ancestor)

            if node.left:
                if not (node.left.val < node.val):
                    return False
                else:
                    # check the left subtree
                    w, z = node.left.left, node.left.right
                    if w:
                        if not (w.val < node.left.val):
                            return False
                    if z:
                        if not (z.val > node.left.val and z.val < max_ancestor):
                            return False
            if node.right:
                    if not (node.right.val > node.val):
                        return False
                    else:
                        x, y = node.right.left, node.right.right
                        if x:
                            if not (x.val > min_ancestor and x.val < node.right.val):
                                return False
                        if y:
                            if not (y.val > node.right.val):
                                return False

            return dfs(node.left, min_ancestor, max_ancestor) and dfs(node.right, min_ancestor, max_ancestor)

        return dfs(root)