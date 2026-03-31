class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Construct frequency hashmap for counting
        frequency_hashmap = {}
        for num in nums:
            frequency_hashmap[num] = frequency_hashmap.get(num, 0) + 1

        #Construct an array of array, where inner array acts as bucket, 
        # and array index acts as frequency
        array_of_frequency_buckets = [[] for _ in range(len(nums)+1)]

        for num, frequency in frequency_hashmap.items():
            array_of_frequency_buckets[frequency].append(num)

        #Return from the back or flip the array
        return_array = []


        for bucket in reversed(array_of_frequency_buckets):
            for num in bucket:
                if k > len(return_array):
                    return_array.append(num)

        return return_array
        