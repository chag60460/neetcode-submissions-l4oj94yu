class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_pointer = 0
        second_pointer = len(numbers) - 1

        while first_pointer < second_pointer:
            if numbers[first_pointer] + numbers[second_pointer] < target:
                first_pointer += 1
            elif numbers[first_pointer] + numbers[second_pointer] > target:
                second_pointer -= 1
            else:
                return [first_pointer + 1, second_pointer + 1]