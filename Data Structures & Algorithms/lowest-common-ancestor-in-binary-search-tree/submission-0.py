# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # so we need to figure out which subtree each solution is in.
        cur = root

        min_node = {
            "node": None
        }

        def get_min_node(min_node, node):
            if min_node["node"] is None:
                min_node["node"] = node

            if node.val < min_node["node"].val:
                min_node["node"] = node


        while cur:
            get_min_node(min_node, cur)
            # our nodes in different subtrees. 
            if cur.val > p.val and cur.val < q.val:
                return min_node["node"]
            elif cur.val > q.val and cur.val < p.val:
                return min_node["node"]

            # now we need to look into the case where either p or q could be an ancestor.
            if cur.val == p.val or cur.val == q.val:
                return min_node["node"]

            # both solutions in left subtree.
            if p.val <= cur.val and q.val <= cur.val:
                cur = cur.left
            # solutions in right subtree.
            elif p.val > cur and q.val > cur:
                cur = cur.right