class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores (start_index, height) in increasing height order
        max_area = 0

        for i, height in enumerate(heights):
            start = i  # track how far left the current bar can extend

            while stack and height < stack[-1][1]:
                # current bar is shorter, so pop and calculate area
                prev_start, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_start))

                # inherit the left boundary of the popped bar
                start = prev_start

            stack.append((start, height))

        # remaining bars in stack extend to the end of the array
        for start, height in stack:
            max_area = max(max_area, height * (len(heights) - start))

        return max_area