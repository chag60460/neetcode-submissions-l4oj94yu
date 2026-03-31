class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Construct frequency hashmap: key - num, value - frequency
        frequency_hashmap = {}

        for num in nums:
            frequency_hashmap[num] = frequency_hashmap.get(num, 0) + 1

        #Can't sort, so use buckets
        frequency_bucket = [[] for _ in range(len(nums))]

        for num, frequency in frequency_hashmap.items():
            frequency_bucket[frequency-1].append(num)

        output_array = []

        #Access from the back
        for bucket_array in frequency_bucket[::-1]:
            if len(output_array) < k:
                output_array.extend(bucket_array)
        
        return output_array