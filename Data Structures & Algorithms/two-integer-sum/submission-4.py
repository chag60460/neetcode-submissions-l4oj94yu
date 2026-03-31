class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_so_far = {}

        #iterate through the nums, with index 
        for i, num in enumerate(nums):
            #check if it has a complement in the list
            complement = target - num
            
            if complement in seen_so_far:
                return [seen_so_far[complement], i]
            
            #if not, store it as a potential complement
            seen_so_far[num] = i