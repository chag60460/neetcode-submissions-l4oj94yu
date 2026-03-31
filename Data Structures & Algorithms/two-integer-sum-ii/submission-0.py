class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(numbers)):
            difference = target - numbers[i]

            if difference in complement:
                return [complement[difference] + 1, i + 1]
            
            complement[numbers[i]] = i

        return []