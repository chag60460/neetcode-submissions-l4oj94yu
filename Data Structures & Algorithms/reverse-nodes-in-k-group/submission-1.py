# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        new_head = None
        prev_head_to_relink = None

        while start:
            counter = 0
            check = start

            #check if we can reverse
            while counter < k - 1 and check:
                counter += 1
                check = check.next
            
            #start reversing
            if check:
                counter = 0
                prev = None
                old_head = start
                
                #reverse until we finish
                while counter < k:
                    temp = start.next
                    start.next = prev
                    prev = start
                    start = temp
                    counter += 1

                if not new_head:
                    new_head = prev

                if prev_head_to_relink:
                    prev_head_to_relink.next = prev
                
                old_head.next = start
                prev_head_to_relink = old_head

            else:
                break    
        return new_head if new_head else head


            