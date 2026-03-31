class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output_set_array = set()

        for i in range(len(sorted_nums)):
            left, right = i + 1, len(sorted_nums) - 1
            target = 0 - sorted_nums[i]
            while left < right:
                if sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                elif sorted_nums[left] + sorted_nums[right] > target:
                    right -= 1
                else:
                    output_set_array.add((sorted_nums[i], sorted_nums[left], sorted_nums[right]))
                    left += 1
                    right -= 1

        return [list(triplet) for triplet in output_set_array]
