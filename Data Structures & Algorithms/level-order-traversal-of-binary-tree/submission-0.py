# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = []
        queue.append(root)
        res = []

        cur_val = 0


        while queue:
            # queue len
            q_len = len(queue)
            res.append([])

            for _ in range(q_len):
                node = queue.pop(0)
                res[cur_val].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            cur_val += 1

        return res