class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ##Approach 1 - O(n^2) because (n-1) + (n-2) + .. 1 = (n)(n-1)/2
        #i stays at the front, j loops the remainder
        # i = 0
        # j = i + 1

        # #check the sum each time

        # #if sum == target, return i and j

        # #if j is exhausted, move i

        # target_found = False

        # while not target_found:
            
        #     current_sum = nums[i] + nums[j]
            
        #     if (current_sum == target):
        #         return [i, j]
        #     elif (j == len(nums) - 1):
        #         i += 1
        #         j = i + 1
        #     else:
        #         j += 1

        ## Approach 2
        
        #store number we've seen and their index in hashmap
        seen_complements = {}
        
        # loop through nums, with index and number
        for i, num in enumerate(nums):
            complement = target - num
            
            #if matching complement is already there, return
            if complement in seen_complements:
                return [seen_complements[complement], i]
            
            #otherwise continue looking for the next potential matching number and udpate hashmap
            seen_complements[num] = i