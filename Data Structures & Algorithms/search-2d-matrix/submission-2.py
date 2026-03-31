class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            midpoint = (left + right) // 2
            midpoint_val = matrix[midpoint // n][midpoint % n]

            if target > midpoint_val:
                left = midpoint + 1
            elif target < midpoint_val:
                right = midpoint - 1
            else:
                return True
        
        return False