# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid
        ref = mid = head
        while ref != None and ref.next != None:
            mid = mid.next
            ref = ref.next.next
        
        # reverse second half
        prev = None
        curr = mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge the first half and the second half
        ref1 = head
        while prev.next != None:
            temp = ref1.next
            temp2 = prev.next
            ref1.next = prev
            prev.next = temp
            ref1 = temp
            prev = temp2