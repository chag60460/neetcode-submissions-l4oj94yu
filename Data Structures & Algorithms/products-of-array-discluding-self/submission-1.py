class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output_array = [1] * len(nums)

        prefix = 1
        suffix = 1
        
        #Loop through nums, accumulating the prefix product
        for index in range(len(nums)):
            output_array[index] = prefix
            prefix *= nums[index]

        #Loop through nums backward, thus accumulating the suffix product
        for index in range(len(nums) - 1, -1, -1):
            output_array[index] *= suffix
            suffix *= nums[index]
        
        return output_array