# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        
        num = []
        while head.next:
            num.append(head.val)
            head = head.next
        num.append(head.val)
        
        n = len(num)
        pt1, pt2 = n//2, n//2
        if len(num)%2 == 0:
            pt1 -= 1
            
        while pt1 >= 0:
            if num[pt1] == num[pt2]:
                pt1 -= 1
                pt2 += 1
            else:
                return False
        return True
            
        