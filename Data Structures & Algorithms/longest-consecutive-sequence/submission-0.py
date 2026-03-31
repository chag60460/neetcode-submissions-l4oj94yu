class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence_length = 0


        for num in nums:

            if num - 1 not in nums_set:

                #potential starter, check for num + 1
                current_sequence_length = 1
                while num + 1 in nums_set:

                    #Go to the next one and continue checking, also increment current_sequence_length
                    num += 1
                    current_sequence_length += 1

                #Increment sequence length
                if current_sequence_length > max_sequence_length:
                    max_sequence_length = current_sequence_length
        
        return max_sequence_length