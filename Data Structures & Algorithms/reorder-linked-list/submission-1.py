# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        #find the middle
        slow,fast = head,head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        #reverse the second list
        curr= slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next= prev
            prev= curr
            curr= temp
        #merge the 2 lists
        first,last = head, prev
        while last:
            temp1, temp2 = first.next,last.next
            first.next = last
            last.next = temp1
            first, last = temp1,temp2

