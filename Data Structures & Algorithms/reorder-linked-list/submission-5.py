# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid_pointer = head
        end_pointer = head

        while end_pointer.next and end_pointer.next.next:
            end_pointer = end_pointer.next.next
            mid_pointer = mid_pointer.next
        
        l2 = mid_pointer.next
        mid_pointer.next = None

        #reverse second list
        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        l2 = prev

        #connect the two lists
        l1 = head
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next
