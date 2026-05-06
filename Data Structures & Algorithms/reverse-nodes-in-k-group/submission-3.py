# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #dummy node to get to kth_node
        start = ListNode(0, head)
        start_pointer = start

        #check if we have enough node to form a group of k
        while True:
            kth_node = self.get_kth_node(start_pointer, k)

            if not kth_node:
                break
            
            #reverse the group of k nodes
            prev, next_group = kth_node.next, kth_node.next
            current = start_pointer.next
            
            while current != next_group:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            #move start pointer to next group
            group_tail = start_pointer.next
            start_pointer.next = prev
            start_pointer = group_tail

        return start.next

    def get_kth_node(self, start_node, k):
        while start_node and k > 0:
            start_node = start_node.next
            k -= 1

        return start_node