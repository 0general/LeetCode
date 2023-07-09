# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ls = [head]
        nx = head.next
        while nx:
            ls.append(nx)
            nx = nx.next
        idx = len(ls) - n
        if idx == 0:
            if len(ls) != 1:
                return ls[1]
            else:
                return None
        else:
            if idx == len(ls) - 1:
                ls[idx-1].next = None
            else:
                ls[idx-1].next = ls[idx+1]
            return ls[0]
        