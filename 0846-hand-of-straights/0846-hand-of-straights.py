class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = {}
        for c in hand:
            cards[c] = 1 + cards.get(c, 0)
        
        min_heap = list(cards.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            for i in range(groupSize):
                if min_heap[0] + i not in cards:
                    return False
                if cards[min_heap[0] + i] <= 0:
                    return False
                cards[min_heap[0] + i] -= 1
            while min_heap and cards[min_heap[0]] == 0:
                cards.pop(min_heap[0])
                heapq.heappop(min_heap)
            
        return True if not cards else False