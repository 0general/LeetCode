# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while True:
            if head is None:
                break
            ans.append(head)
            head = head.next
        if len(ans):
            return ans[len(ans)//2]
        else:
            return ans