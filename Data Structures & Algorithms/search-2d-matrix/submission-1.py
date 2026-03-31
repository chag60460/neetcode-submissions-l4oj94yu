class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        m_left, m_right = 0, m - 1
        
        n = len(matrix[0])
        n_left, n_right = 0, n - 1

        while m_left <= m_right:
            m_midpoint = int((m_right + m_left) / 2)
            n_midpoint = int((n_right + n_left) / 2)
            midpoint_val = matrix[m_midpoint][n_midpoint]

            if target > midpoint_val:
                if n_left < n_right:
                    n_left = n_midpoint + 1
                else:
                    m_left += 1
                    n_left = 0

            elif target < midpoint_val:
                if n_right > n_left:
                    n_right = n_midpoint - 1
                else:
                    m_right -= 1
                    n_right = n - 1
            else:
                return True
        
        return False