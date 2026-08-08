# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        l=r=dummy
        while n>0:
            r= r.next
            n-=1
        
        prev = None
        while r:
            prev = l
            l= l.next
            r=r.next
        prev.next = l.next

        return dummy.next

        
                
            


        