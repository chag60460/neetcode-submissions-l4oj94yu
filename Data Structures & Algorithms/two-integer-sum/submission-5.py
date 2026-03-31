class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a hashmap to keep track of numbers we've seen so far
        seen_so_far = {}

        #Loop through the list
        for i in range(len(nums)):
            
            #Compute complement
            complement = target - nums[i]

            # If complement is in set, that means we found a match!
            if complement in seen_so_far:
                return [seen_so_far[complement], i]
            
            #If we don't have a match, add the num and index to the hashmap
            else:
                seen_so_far[nums[i]] = i