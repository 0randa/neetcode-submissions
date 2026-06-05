# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # function to get the height of each subbranch.
        def height(node) -> int:
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)

            return max(left, right) + 1

        balanced = True
        def dfs(node) -> bool:
            nonlocal balanced
            if node is None:
                return balanced

            left_height = height(node.left)
            right_height = height(node.right)

            # print(f"{node.val}, {left_height}, {right_height}")

            difference = abs(left_height - right_height)
            print(difference)
            if difference > 1:
                # print("hi")
                balanced = False

            # print(left_height, right_height)
            left = dfs(node.left)
            right = dfs(node.right)

            return balanced

        ans = dfs(root)
        # print(ans)
        return ans
        