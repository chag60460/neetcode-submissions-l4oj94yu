# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            #store next in a temp var to keep track
            temp = current.next
            #flip current pointer to prev
            current.next = previous #node.next = None
            #re-set prev to current
            previous = current
            #go to next one through stored value
            current = temp #current = old nod.next

        return previous