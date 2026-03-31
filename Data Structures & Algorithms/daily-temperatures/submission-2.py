class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_array = [0] * len(temperatures)

        #stack to keep track of temps until we hit a local maximum to the right
        decreasing_stack = []
        
        for index, temp in enumerate(temperatures):
            #If current temp > top of stack, pop and compute index
            while decreasing_stack and  temp > decreasing_stack[-1][1]:
                popped_index, popped_temp = decreasing_stack.pop(-1)
                output_array[popped_index] = index - popped_index
            decreasing_stack.append((index, temp))

        
        return output_array