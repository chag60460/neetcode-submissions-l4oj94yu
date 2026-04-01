class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            if heights[left] < heights[right]:
                max_area = max(max_area, heights[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, heights[right] * (right - left))
                right -= 1
        
        return max_area