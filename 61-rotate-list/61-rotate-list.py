# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0
        
    def length(self):
        self.num = 0
        node = self.head
        while node is not None:
            self.num += 1
            if node.next is None:
                self.tail = node
                break
            node = node.next
            
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.head = head
        self.length()
        if self.num == 0 or self.num == 1:
            return self.head
        
        k %= self.num
        
        for _ in range(self.num-k):
            node = ListNode()
            node.val = self.head.val
            node.next = None
            self.head = self.head.next
            self.tail.next = node
            self.tail = node
        
        return self.head
            
        
        