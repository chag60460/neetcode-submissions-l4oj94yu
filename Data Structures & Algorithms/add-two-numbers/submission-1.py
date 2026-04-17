# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        start_node = ListNode(0, None)
        pointer = start_node

        while l1 and l2:
            pointer.next = ListNode(l1.val + l2.val, None)
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next
        
        pointer.next = l1 or l2
        
        carry_pointer = start_node
        while carry_pointer:
            if carry_pointer.val >= 10:
                carry = carry_pointer.val % 10
                digit = carry_pointer.val // 10
                carry_pointer.val = carry

                if not carry_pointer.next:
                    carry_pointer.next = ListNode(digit, None)
                else:
                    carry_pointer.next.val += digit
            
            carry_pointer = carry_pointer.next
        
        return start_node.next