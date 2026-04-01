class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_array = [0] * len(temperatures)
        tracking_stack = []
        for index, temp in enumerate(temperatures):
            while tracking_stack and temp > tracking_stack[-1][1]:
                element_index = tracking_stack.pop(-1)[0]
                output_array[element_index] = index-element_index
            
            tracking_stack.append([index,temp])
        return output_array