# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        node= head
        stack= []

        #find the tail
        while node:
            stack.append(node)
            node = node.next

        curr= head
        n = len(stack)
        for i in range(n//2):
            tail = stack.pop()
            temp= curr.next
            curr.next = tail
            tail.next= temp
            curr = temp
        
        curr.next = None

       
        

        