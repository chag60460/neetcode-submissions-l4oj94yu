class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output_array = [0] * len(temperatures)
        non_identified_days_stack = []

        for index, temperature in enumerate(temperatures):
            while non_identified_days_stack and temperature > non_identified_days_stack[-1][1]:
                popped_index, popped_temp = non_identified_days_stack.pop(-1)
                output_array[popped_index] = index - popped_index
            non_identified_days_stack.append((index, temperature))
        
        return output_array

