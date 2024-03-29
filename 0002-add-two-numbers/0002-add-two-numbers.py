# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        
        pointer = node
        c = 0
        while l1 or l2 or c:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            
            s = n1 + n2+ c
            c = s // 10
            
            pointer.next = ListNode(s % 10)
            
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return node.next
            
        
        