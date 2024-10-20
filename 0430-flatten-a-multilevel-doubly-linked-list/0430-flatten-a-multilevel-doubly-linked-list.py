"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        next_list = []
        curr = head
        while curr:
            if curr.next:
                next_list.append(curr.next)
                curr.next = None
            if curr.child:
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None
            if curr.next is None and next_list:
                node = next_list.pop()
                node.prev = curr
                curr.next = node
            curr = curr.next
        return head
                
                