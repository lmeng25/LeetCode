# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        pq = []
        for head in lists:
            while head:
                heapq.heappush(pq, head.val)
                head = head.next
        
        if not pq:
            return None
        
        head = ListNode(heapq.heappop(pq))
        ref = head
        while pq:
            ref.next = ListNode(heapq.heappop(pq))
            ref = ref.next
            
        return head