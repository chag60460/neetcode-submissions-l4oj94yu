class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count the frequency of each number and store in a hashmap
        frequency_hash = {}

        for num in nums:
            frequency_hash[num] = frequency_hash.get(num, 0) + 1

        # Create buckets storing each number based on its frequency
        # An array of arrays, where the index of the array correponds to frequency
        # Each array is a potential frequency bucket, storing the numbers with that frequency
        frequency_buckets = [ [] for _ in range(len(nums)) ]

        for num, frequency in frequency_hash.items():
            frequency_buckets[frequency-1].append(num)

        # Loop backwards
        return_list = []
        for bucket_index in range(len(nums)-1, -1, -1):
            for num in frequency_buckets[bucket_index]:
                if len(return_list) < k:
                    return_list.append(num)
        
        return return_list