class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            
            #previous item in stack not extendable to the right, so we compute the area right away
            while stack and stack[-1][1] > height:
                leftmost_extendable_index, leftmost_extendable_index_height = stack.pop(-1)
                maxArea = max(maxArea, leftmost_extendable_index_height*(i - leftmost_extendable_index))
                
                start = leftmost_extendable_index #update start by extending it to the left
    
            stack.append((start, height)) #append new (or original) start value along with the height

        for remaining_index, remaining_height in stack:
            maxArea = max(maxArea, (len(heights) - remaining_index) * remaining_height)
    
        return maxArea