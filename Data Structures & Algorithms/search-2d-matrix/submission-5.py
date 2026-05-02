class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m*n - 1

        while left <= right:
            midpoint = (left + right) // 2
            row_index = midpoint // n
            column_index = midpoint % n
            midpoint_value = matrix[row_index][column_index]

            if target < midpoint_value:
                right = midpoint - 1

            elif target > midpoint_value:
                left = midpoint + 1
            
            else:
                return True
        
        return False