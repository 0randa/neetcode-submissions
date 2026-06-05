# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        curr = head

        linked_list_length = 0

        while curr:
            linked_list_length += 1
            curr = curr.next

        to_remove = linked_list_length - n

        curr = head
        for i in range(to_remove - 1):
            print(curr.val)
            curr = curr.next

        if not to_remove:
            return head.next

        bob = curr.next.next

        curr.next = bob

        return head


