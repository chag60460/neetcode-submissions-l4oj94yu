# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        prev_head_pointer_to_relink = None
        new_head = None

        while start:
            counter = 0
            check = start

            while counter < k and check:
                counter += 1
                check = check.next

            if counter == k:
                counter = 0
                prev = None
                prev_head = start
                
                while k > counter:
                    temp = start.next
                    start.next = prev
                    prev = start
                    start = temp

                    counter += 1
                
                if not new_head:
                    new_head = prev
                if prev_head_pointer_to_relink: 
                    prev_head_pointer_to_relink.next = prev
                
                prev_head.next = start
                prev_head_pointer_to_relink = prev_head

            else:
                break
        return new_head if new_head else head
                