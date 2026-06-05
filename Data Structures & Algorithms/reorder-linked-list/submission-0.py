# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        first, second = self.splitList(head)

        reverse_second = self.reverseList(second)


        curr1 = first
        curr2 = reverse_second

        while (curr1) and (curr2):
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2

        self.printList(curr1)
        

    def splitList(self, head):
        fast, slow = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None
        
        return head, slow


    def reverseList(self, head):
      
        # Create a stack to store the nodes
        stack = []
    
        temp = head
    
        # Push all nodes except the last node into stack
        while temp.next is not None:
            stack.append(temp)
            temp = temp.next
    
        # Make the last node as new head of the linked list
        head = temp
    
        # Pop all the nodes and append to the linked list
        while stack:
            
            # append the top value of stack in list
            temp.next = stack.pop()
            
            # move to the next node in the list
            temp = temp.next
    
        # Update the next pointer of last node 
        # of stack to None
        temp.next = None
    
        return head


    def printList(self, node):
        while node is not None:
            print(f" {node.val}", end="")
            node = node.next
        print()