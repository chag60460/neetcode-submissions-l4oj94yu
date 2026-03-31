class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = 1
        suffix_product = 1
        output_array = []
        
        for num in nums:
            output_array.append(prefix_product)
            prefix_product *= num

        for i in range(len(nums) - 1, -1, -1):
            output_array[i] *= suffix_product
            suffix_product *= nums[i]
        
        return output_array
