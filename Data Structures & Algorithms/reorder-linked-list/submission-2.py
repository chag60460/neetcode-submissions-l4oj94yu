# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Split the list
        mid_pointer, end_pointer = head, head

        while end_pointer.next and end_pointer.next.next:
            end_pointer = end_pointer.next.next
            mid_pointer = mid_pointer.next

        l2 = mid_pointer.next
        mid_pointer.next = None
        
        #Reverse second list
        prev = None

        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        l2 = prev

        #Merge
        while head and l2:
            head_next = head.next
            l2_next = l2.next

            head.next = l2
            l2.next = head_next

            l2 = l2_next
            head = head_next
            