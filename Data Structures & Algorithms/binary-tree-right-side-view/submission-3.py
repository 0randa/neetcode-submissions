# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        def level_order_traversal(root):
            if not root:
                return []
            res = []
            queue = []
            # enqueue root.
            queue.append(root)

            cur_val = 0

            while queue:
                queue_len = len(queue)
                res.append([])

                for _ in range(queue_len):
                    node = queue.pop(0)
                    res[cur_val].append(node)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                cur_val += 1
            return res
        
        
        res = level_order_traversal(root)

        result = []

        for r in res:
            result.append(r[-1].val)

        return result
