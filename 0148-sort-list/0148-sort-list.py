# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = []
        while head:
            h.append(head.val)
            head = head.next
        h.sort()
        if not h:
            return head
        for i in range(len(h)):
            h[i] = ListNode(h[i])
            if i != 0:
                h[i-1].next = h[i]
        return h[0]
            
        