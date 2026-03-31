class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer, right_pointer = 0, len(height) - 1
        left_max, right_max = height[left_pointer], height[right_pointer]
        total_water = 0

        while left_pointer < right_pointer:
            if left_max < right_max:
                left_pointer += 1
                total_water += max(0, left_max - height[left_pointer])
                left_max = max(left_max, height[left_pointer])
            else:
                right_pointer -= 1
                total_water += max(0, right_max - height[right_pointer])
                right_max = max(right_max, height[right_pointer])
        
        return total_water