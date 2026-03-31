class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use A hashtable of sets (hashsets) to store everything
        row_hashset = collections.defaultdict(set)
        column_hashset = collections.defaultdict(set)
        box_hashset = collections.defaultdict(set)

        #Loop
        for row_index in range(9):
            for column_index in range(9):
                sudoku_value = board[row_index][column_index]

                if sudoku_value != ".":

                    #Check duplicate
                    if (sudoku_value in row_hashset[row_index] or
                        sudoku_value in column_hashset[column_index] or
                        sudoku_value in box_hashset[(row_index // 3, column_index // 3)]):
                        return False
                    
                    row_hashset[row_index].add(sudoku_value)
                    column_hashset[column_index].add(sudoku_value)
                    box_hashset[(row_index // 3, column_index // 3)].add(sudoku_value)
        
        return True