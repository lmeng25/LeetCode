class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        total = 0
        res = 0
        for i in range(len(diff)):
            if diff[i] + total < 0:
                total = 0
                res = i + 1
            else:
                total += diff[i]
        
        return res