class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        frequency_hashmap = {}
        
        for num in nums:
            frequency_hashmap[num] = frequency_hashmap.get(num, 0) + 1
            if frequency_hashmap[num] > 1:
                return True
        
        return False
