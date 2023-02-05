# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: # 바꿀 게 없음
            return head
        # 바꿀 게 있음
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next
        
        