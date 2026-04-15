# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start_pointer = ListNode(0, head)
        before_n_pointer,end_pointer = start_pointer, head

        while n:
            end_pointer = end_pointer.next
            n -= 1
        
        while end_pointer:
            end_pointer = end_pointer.next
            before_n_pointer = before_n_pointer.next

        before_n_pointer.next = before_n_pointer.next.next
        return start_pointer.next