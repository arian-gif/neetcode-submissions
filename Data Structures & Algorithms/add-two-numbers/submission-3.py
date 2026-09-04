# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        sol = 0

        while l1 or l2:
            first, second = 0,0
            if l1:
                first = l1.val
                l1 = l1.next
            if l2:
                second = l2.val
                l2 = l2.next
            sol += (first+second)*10**n
            n+=1
        temp = dummy = ListNode()
        if sol == 0:
            return dummy
        while sol>0:
            val = sol % 10
            curr = ListNode(val=val)
            temp.next = curr
            temp = temp.next
            sol = sol//10
            
        return dummy.next