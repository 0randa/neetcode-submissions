class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify initialization
        dummy = ListNode(-1)
        curr = dummy

        # Traverse both lists
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # Add remaining nodes from list1 or list2
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2

        # Return the merged list starting at dummy.next
        return dummy.next