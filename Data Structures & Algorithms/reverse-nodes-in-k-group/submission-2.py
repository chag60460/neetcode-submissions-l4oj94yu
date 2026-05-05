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

            #make sure each group has k nodes
            kth_node = self.get_kth(start_pointer, k)

            if not kth_node:
                break
            
            next_group_start_node = kth_node.next
            
            #reverse each group
            prev = next_group_start_node
            current = start_pointer.next

            while current != next_group_start_node:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            #reset start pointer
            temp = start_pointer.next 
            start_pointer.next = kth_node #on first iteration, it resets dummy to kth_node. On consequent iteration, it links original start node with next group's original kth_node
            start_pointer = temp

        return start.next
        
    def get_kth(self, start_node, k):
        while start_node and k > 0:
            start_node = start_node.next
            k -= 1
        
        return start_node