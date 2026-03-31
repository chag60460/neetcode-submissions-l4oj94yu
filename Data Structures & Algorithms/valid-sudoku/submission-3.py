class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        column_hash = defaultdict(set)
        box_hash = defaultdict(set)
        
        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                cell_value = board[row_index][column_index]
                box_tuple = (row_index // 3, column_index // 3)
                if cell_value != ".":
                    if cell_value in row_hash[row_index] or cell_value in column_hash[column_index] or cell_value in box_hash[box_tuple]:
                        return False
                    
                    row_hash[row_index].add(cell_value)
                    column_hash[column_index].add(cell_value)
                    box_hash[box_tuple].add(cell_value)
                

        return True