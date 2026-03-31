class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #i stays at the front, j loops the remainder
        i = 0
        j = i + 1

        #check the sum each time

        #if sum == target, return i and j

        #if j is exhausted, move i

        target_found = False

        while not target_found:
            
            current_sum = nums[i] + nums[j]
            
            if (current_sum == target):
                return [i, j]
            elif (j == len(nums) - 1):
                i += 1
                j = i + 1
            else:
                j += 1