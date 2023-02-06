class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        i = 0;
        
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        
        return [i+1, j+1]
            