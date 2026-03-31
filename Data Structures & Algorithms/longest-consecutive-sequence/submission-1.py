class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Keep track of longest sequence
        longest_sequence = 0
        

        #Use set for constant time lookup
        nums_set = set(nums)

        for num in nums_set:

            #Check to see if it could be the start of a sequence
            if num - 1 not in nums_set:
                current_sequence_length = 0
                start = num
                
                while start in nums_set:
                    current_sequence_length += 1
                    start += 1

                longest_sequence = max(longest_sequence, current_sequence_length)
        
        return longest_sequence
                
