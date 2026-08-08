# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l1,l2= list1,list2
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2== None:
            return l1

        while l1 or l2:
            if l1 is None:
                curr.next = l2
                break
            elif l2 is None:
                curr.next = l1
                break
            elif l1.val>=l2.val:
                curr.next= l2
                l2= l2.next
            elif l2.val>l1.val:
                curr.next= l1
                l1=l1.next
            curr= curr.next
            print(l1.val if l1 else None,l2.val if l2 else None)
        return dummy.next
            

        


        