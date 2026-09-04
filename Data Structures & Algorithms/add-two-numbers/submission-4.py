# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry!=0:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1=0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2=0
            val = v1+v2+carry
            carry = val//10
            val = val %10
            
            curr = ListNode(val)
            temp.next = curr
            temp = temp.next
        
        return dummy.next
        