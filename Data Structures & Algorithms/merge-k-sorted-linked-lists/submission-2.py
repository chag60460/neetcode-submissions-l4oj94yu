# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        merged = lists[0]

        for i in range(1, len(lists)):
            merged = self.mergeTwoLists(merged, lists[i])
        
        return merged
        
    def mergeTwoLists(self, l1, l2):
        start = ListNode()
        start_pointer = start

        while l1 and l2:
            if l1.val < l2.val:
                start_pointer.next = l1
                l1 = l1.next
            else:
                start_pointer.next = l2
                l2 = l2.next
            
            start_pointer = start_pointer.next
        
        start_pointer.next = l1 if l1 else l2

        return start.next
            