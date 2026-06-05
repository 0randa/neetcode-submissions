# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        arr1, arr2 = [], []
        def dfs(node1, node2) -> None:
            nonlocal arr1
            nonlocal arr2
            if not node1 and not node2:
                return 
            
            if not node1 or not node2:
                if not node1:
                    arr1.append(None)
                else:
                    arr1.append(node1.val)

                if not node2:
                    arr2.append(None)
                else:
                    arr2.append(node2.val)
                return 
            

            arr1.append(node1.val)
            arr2.append(node2.val)

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p,q)
        return arr1 == arr2
