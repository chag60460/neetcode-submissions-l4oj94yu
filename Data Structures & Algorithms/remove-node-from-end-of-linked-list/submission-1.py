# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offset_node = ListNode(0, head)
        before_n_pointer = offset_node
        end_pointer = head

        while n:
            end_pointer = end_pointer.next
            n -= 1
        
        while end_pointer:
            end_pointer = end_pointer.next
            before_n_pointer = before_n_pointer.next

        before_n_pointer.next = before_n_pointer.next.next

        return offset_node.next