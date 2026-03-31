class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        output_set = set()

        for i in range(len(sorted_nums)):
            
            first_pointer = i + 1
            second_pointer = len(nums) - 1
            target = 0 - sorted_nums[i]
            
            while first_pointer < second_pointer:
                if sorted_nums[first_pointer] + sorted_nums[second_pointer] < target:
                    first_pointer += 1
                elif sorted_nums[first_pointer] + sorted_nums[second_pointer] > target:
                    second_pointer -= 1
                else:
                    output_set.add((sorted_nums[i], sorted_nums[first_pointer], sorted_nums[second_pointer]))
                    first_pointer += 1
                    second_pointer -= 1
                
        return list(output_set)
