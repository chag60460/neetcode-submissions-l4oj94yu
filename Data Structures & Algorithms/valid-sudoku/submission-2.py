class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use hash sets to store our data for O(1) access time
        columns_hash = collections.defaultdict(set)
        boxes_hash = collections.defaultdict(set)

        for row_index in range(9):
            
            row_hash = set()
            row = board[row_index]
            
            for column_index in range(9):
                
                cell_value = row[column_index]
                box_tuple = (row_index // 3, column_index // 3)

                if cell_value != ".":
                    
                    if cell_value not in row_hash and cell_value not in columns_hash[column_index] and cell_value not in boxes_hash[box_tuple]:
                            row_hash.add(cell_value)
                            columns_hash[column_index].add(cell_value)
                            boxes_hash[box_tuple].add(cell_value)
                    else:
                        return False

        return True