class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, suffix = 1, 1
        output_array = []

        for num in nums:
            output_array.append(prefix)
            prefix *= num

        for i in range(len(nums) - 1, -1, -1):
            output_array[i] *= suffix
            suffix *= nums[i]
        
        return output_array