# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #split the list
        mid, end = head, head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        p2 = mid.next
        mid.next = None
        
        #reverse second list
        prev = None
        
        while p2:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        
        p2 = prev
        
        #merge
        p1 = head

        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next
            
            p1 = p1_next
            p2 = p2_next
