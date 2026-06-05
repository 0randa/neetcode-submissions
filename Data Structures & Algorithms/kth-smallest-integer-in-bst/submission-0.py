# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        num = 0
        ret_val = 0
        def inOrder(node):
            nonlocal num
            nonlocal ret_val
            if not node:
                return

            inOrder(node.left)
            
            num += 1

            print(node.val, num, k)

            if num == k:
                print("hey")
                ret_val = node.val

            inOrder(node.right)

        inOrder(root)
        return ret_val