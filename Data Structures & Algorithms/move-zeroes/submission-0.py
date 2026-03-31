class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Loop through the lsit
        # keep track of last zero position to insert

        swapIndex = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                swapIndex += 1
