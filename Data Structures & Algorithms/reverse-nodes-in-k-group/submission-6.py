# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        start_pointer = start

        while True:
            kth_node = self.get_kth_node(start_pointer, k)
            
            if not kth_node:
                break
            
            #reverse each group
            prev = kth_node.next
            current = start_pointer.next
            next_group_start_node = kth_node.next
            
            while current != next_group_start_node:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            temp = start_pointer.next
            start_pointer.next = kth_node
            start_pointer = temp
        
        return start.next

    def get_kth_node(self, start_node, k):
        while start_node and k:
            start_node = start_node.next
            k -= 1
        
        return start_node