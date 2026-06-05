# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        prev = None
        while curr:
            # reference the next item
            temp = curr.next


            # the head is detached at the start?
            curr.next = prev

            # print("current", curr.val)


            # print("the new curr next", curr.next.val)

            # print("next", next.val)

            # set the previous to current
            prev = curr

            # set the current to next
            curr = temp

            print()
        return prev