# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 참고 : https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/3521559/Python3-Easy-with-comments
        dummy = ListNode()
        prev_group = dummy
        while head:
            j, group_end = 1, head
            while j < k and head.next:
                head = head.next
                j += 1
            group_start = head
            next_group = head = head.next
            
            if j != k:
                break
            prev, cur = None, group_end
            while cur != next_group:
                cur.next, cur, prev = prev, cur.next, cur
            
            prev_group.next = group_start
            prev_group = group_end
            group_end.next = next_group
        
        return dummy.next