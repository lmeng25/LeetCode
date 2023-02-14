class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        time = [float(target - pos) / sp for pos, sp in sorted(zip(position, speed))]

        curr = 0
        for car in time[::-1]:
            if car > curr:
                res += 1
                curr = car
                
        return res
        