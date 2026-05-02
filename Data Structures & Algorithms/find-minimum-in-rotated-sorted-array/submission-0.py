class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid_point = (left + right) // 2

            if nums[mid_point] > nums[right]:
                #min is to the right of midpoint
                left = mid_point + 1
            else:
                #min is at or to the left of midpoint
                right = mid_point
        
        return nums[left]