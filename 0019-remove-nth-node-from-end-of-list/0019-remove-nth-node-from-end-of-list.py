# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        ref = head
        while ref:
            ref = ref.next
            length += 1
        
        if length == 1:
            return None
        
        if length == n:
            return head.next
        
        ref1 = ListNode(-1, head)
        for i in range(length - n - 1):
            head = head.next
        
        head.next = head.next.next
        
        return ref1.next