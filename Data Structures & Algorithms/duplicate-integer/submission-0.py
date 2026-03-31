class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Store frequency in a hashmap
        frequency_hashmap = {}

        for num in nums:
            if num in frequency_hashmap:
                return True
            else:
                frequency_hashmap[num] = 1
        
        return False