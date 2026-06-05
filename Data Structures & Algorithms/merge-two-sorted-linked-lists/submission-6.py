# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1
        
        head1, head2 = list1, list2
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            temp1, temp2 = curr1.next, curr2.next       

            if curr1.val <= curr2.val:
                curr1.next = curr2
                curr1 = temp1
            elif curr2.val < curr1.val:
                curr2.next = curr1
                curr2 = temp2

        if not curr1:
            return head1
        if not curr2:
            return head2
