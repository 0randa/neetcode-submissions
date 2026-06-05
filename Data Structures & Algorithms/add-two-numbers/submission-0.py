# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        cur = head

        carry_over = False

        while l1 and l2:
            
            node_val = l1.val + l2.val 

            if node_val >= 10:
                carry_over = True
                node_val -= 10


            node = ListNode(node_val)
            cur.next = node
            cur = cur.next
            
            l1 = l1.next
            l2 = l2.next

        if carry_over:
            cur.next = ListNode(1)

        return head.next