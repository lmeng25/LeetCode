# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        ref = head
        while list1 and list2:
            if list1.val < list2.val:
                ref.next = list1
                list1 = list1.next
            else:
                ref.next = list2
                list2 = list2.next
            ref = ref.next
        
        if list1:
            ref.next = list1
        
        if list2:
            ref.next = list2
            
        return head