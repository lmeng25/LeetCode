class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        remain_gas = 0
        res = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if remain_gas + diff < 0:
                remain_gas = 0
                res = i + 1
            else:
                remain_gas += diff
        return res