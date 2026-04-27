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
            merged = self.mergeLists(merged, lists[i])
        
        return merged

    def mergeLists(self, l1, l2):
        dummyNode = ListNode()
        pointer = dummyNode

        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next

            else:
                pointer.next = l2
                l2 = l2.next

            pointer = pointer.next
            
        pointer.next = l1 if l1 else l2

        return dummyNode.next