class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        first_pointer = 0
        second_pointer = len(heights) - 1

        max_container_size = 0

        while first_pointer < second_pointer:
            container_size = min(heights[first_pointer], heights[second_pointer]) * (second_pointer - first_pointer)
            max_container_size = max(max_container_size, container_size)
        
            if heights[first_pointer] > heights[second_pointer]:
                second_pointer -= 1
            else:
                first_pointer += 1
        
        return max_container_size