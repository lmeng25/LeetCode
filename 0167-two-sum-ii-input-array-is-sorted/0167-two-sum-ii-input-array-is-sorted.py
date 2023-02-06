class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(numbers)):
            if numbers[i] in map.values():
                return [list(map.keys())[list(map.values()).index(numbers[i])] + 1, i + 1]
            else:
                map[i] = target - numbers[i]