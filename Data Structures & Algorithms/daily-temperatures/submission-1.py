class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_array = [0] * len(temperatures)
        # Keep a stack, compare each temperature vs with top of stack
        tracking_stack = []

        #If current element <= top of stack or stack is empty, add to stack
        for i, temp in enumerate(temperatures):
            #If current element > top of stack, pop and compute index difference
            while tracking_stack and temp > tracking_stack[-1][1]:
                popped_index, popped_temp = tracking_stack.pop(-1)
                output_array[popped_index] = i - popped_index

            tracking_stack.append((i, temp))

        return output_array
