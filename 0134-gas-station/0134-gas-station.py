class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            if gas[i] - cost[i] + total < 0:
                total = 0
                res = i + 1
            else:
                total += gas[i] - cost[i]
        
        return res