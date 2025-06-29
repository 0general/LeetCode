# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        positions = []
        pos = 1
        prev, curr = head, head.next

        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                positions.append(pos)
            prev, curr = curr, nxt
            pos += 1

        if len(positions) < 2:
            return [-1, -1]

        min_dist = min(b - a for a, b in zip(positions, positions[1:]))
        max_dist = positions[-1] - positions[0]
        return [min_dist, max_dist]
