class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        current_sum = numbers[left_pointer] + numbers[right_pointer]

        while current_sum != target:
            if current_sum < target:
                left_pointer += 1
            else:
                right_pointer -= 1
            current_sum = numbers[left_pointer] + numbers[right_pointer]
        
        return [left_pointer + 1, right_pointer + 1]