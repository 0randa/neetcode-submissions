# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        slow, fast = head, head.next
        slow_index, fast_index = 1, 2

        # have the slow index reach the end.
        while fast and fast.next:
            slow = slow.next
            slow_index += 1
            fast = fast.next.next
            fast_index += 2

        if fast_index == n:
            return head.next


        prev = None
        while fast_index - slow_index != n - 1:
            prev = slow
            slow = slow.next
            slow_index += 1    

        prev.next = slow.next

        return head
    


        
