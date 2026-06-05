# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        curr = head
        prev = None
        listLen = self.getLength(curr)

        if listLen == n:
            return head.next

        index = 0
        while listLen - n != index:
            prev = curr
            curr = curr.next
            index += 1

        prev.next = curr.next


        

        return head
    

    def print_list(self, head):
        while head:
            print(head)
            head = head.next

    def getLength(self, head):
        if head is None:
            return 0
        return 1 + self.getLength(head.next)
        
