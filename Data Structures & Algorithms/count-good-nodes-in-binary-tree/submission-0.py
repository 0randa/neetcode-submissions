# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def bfs(node, max_ancestor):
            nonlocal count
            if node is None:
                return

            max_ancestor = max(max_ancestor, node.val)
            
            if max_ancestor == node.val:
                count += 1

            bfs(node.left, max_ancestor)
            bfs(node.right, max_ancestor)

        bfs(root, root.val)
        return count