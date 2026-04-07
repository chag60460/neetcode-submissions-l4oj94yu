# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            temp = current.next

            #Reverse pointer
            current.next = previous

            #Slide previous forward
            previous = current

            #Slide curent forward
            current = temp
        
        return previous

