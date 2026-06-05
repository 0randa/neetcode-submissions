# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_ancestor, max_ancestor):
            if not node:
                return True

            min_ancestor, max_ancestor = min(node.val, min_ancestor), max(node.val, max_ancestor)

            if node.val == 26:
                print("hey")

            # checking left subtree
            if node.left:
                if node.val == 26:
                    print("hi")
                # left has to be less than current val
                if not (node.left.val < node.val):
                    return False
                else:
                    w, z = node.left.left, node.left.right
                    if w:
                        if not (w.val < node.left.val):
                            return False
                    if z:
                        if node.val == 26:
                            print("heya")
                        # z has to be less than our largest ancestor (5) and greater than
                        # node.left (4)
                        if not (z.val > node.left.val and z.val < max_ancestor):
                            return False
            if node.right:

                if node.val == 26:
                    print("yoo")
                # right node always greater than parent node
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

        return dfs(root, root.val, root.val)