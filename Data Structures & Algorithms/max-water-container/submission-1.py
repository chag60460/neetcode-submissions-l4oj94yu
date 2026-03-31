class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights) - 1
        max_area = 0

        while left_pointer < right_pointer:
            area = min(heights[right_pointer], heights[left_pointer]) * (right_pointer - left_pointer)
            if area > max_area:
                max_area = area
            
            if heights[right_pointer] > heights[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area