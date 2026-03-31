class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Compute an array of prefixes
        prefix = 1
        output_array = [1] * len(nums)

        for index in range(len(nums)):
            #store prefix
            output_array[index] = prefix

            #compute next prefix (mutiply the number itself) and update prefix variable
            prefix *= nums[index]

        #Add in suffixes into the array
        suffix = 1

        for index in range(len(nums) - 1, -1, -1):
            #mutiply prefix product with suffix
            output_array[index] *= suffix
            
            #update suffix with current number
            suffix *= nums[index]
        
        return output_array