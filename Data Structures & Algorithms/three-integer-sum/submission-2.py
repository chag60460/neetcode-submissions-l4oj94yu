class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        output_set = set()
        
        for i in range(len(sorted_array)):
            target = 0 - sorted_array[i]
            first_pointer = i + 1
            second_pointer = len(sorted_array) - 1
            
            while first_pointer < second_pointer:
                if sorted_array[first_pointer] + sorted_array[second_pointer] < target:
                    first_pointer += 1
                elif sorted_array[first_pointer] + sorted_array[second_pointer] > target:
                    second_pointer -= 1
                elif sorted_array[first_pointer] + sorted_array[second_pointer] == target:
                    output_set.add((sorted_array[i], sorted_array[first_pointer], sorted_array[second_pointer]))
                    first_pointer += 1
                    second_pointer -= 1
        
        return [list(triple) for triple in output_set]