class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid_point = (left + right) // 2

            if nums[mid_point] > nums[right]: #we are in the "rotated" side - i.e the big numbers side, so we want to look right
                left = mid_point + 1
            else: #we are in the "sorted" side - i.e the small numbers side
                #this means nothing to the right of mid_point is smaller than mid_point
                #min is either at mid_point, or left of mid_point
                right = mid_point

        return nums[left]