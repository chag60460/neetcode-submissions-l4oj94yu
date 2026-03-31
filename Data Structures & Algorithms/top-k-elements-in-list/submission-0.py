class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_hashmap = {}

        for num in nums:
            frequency_hashmap[num] = frequency_hashmap.get(num, 0) + 1

        # Create buckets to group all the numbers
        # There can be 0-n frequency buckets
        # An array of arrays, where the index corresponds to frequency bucket
        # and inner array contains numbers that fall under this frequency
        frequency_arrays = [[] for _ in range(len(nums) + 1)]
        for num, frequency in frequency_hashmap.items():
            frequency_arrays[frequency].append(num)
        
        # Loop backwards, since we are selecting the k most frequent elements
        return_list = []
        for frequency_index in range(len(frequency_arrays) - 1, 0, -1): 
            for num in frequency_arrays[frequency_index]:
                if len(return_list) < k:
                    return_list.append(num)
        
        return return_list