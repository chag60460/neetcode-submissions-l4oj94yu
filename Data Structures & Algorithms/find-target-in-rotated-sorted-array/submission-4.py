class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid_point = (left + right) // 2

            if nums[mid_point] > nums[right]:
                left = mid_point + 1
            else:
                right = mid_point
        
        min_val_index = left

        if nums[min_val_index] <= target <= nums[-1]:
            return self.binary_search(min_val_index, len(nums) - 1, target, nums)
        else:
            return self.binary_search(0, min_val_index - 1, target, nums)
        
    def binary_search(self, left, right, target, nums):
        while left <= right:
            mid_point = (left + right) // 2

            if nums[mid_point] < target:
                left = mid_point + 1
    
            elif nums[mid_point] > target:
                right = mid_point - 1

            elif nums[mid_point] == target:
                return mid_point
        
        return -1