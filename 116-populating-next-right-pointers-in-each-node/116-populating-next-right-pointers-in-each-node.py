"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        arr = deque()
        arr.append(root)
        while arr:
            temp = deque()
            for _ in range(len(arr)):
                x = arr.popleft()
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
                if len(arr):
                    x.next = arr[0]
                else:
                    arr = temp
        return root
        
        