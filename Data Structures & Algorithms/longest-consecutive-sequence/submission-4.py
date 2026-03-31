class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest_consecutive_sequence = 0
        num_set = set(nums)
        
        for num in nums:
            current_sequence_length = 1
            
            if num-1 not in num_set:
                
                while num + 1 in num_set:
                    current_sequence_length += 1
                    num += 1
                
                if current_sequence_length > longest_consecutive_sequence:
                    longest_consecutive_sequence = current_sequence_length
        
        return longest_consecutive_sequence