class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_hashmap_arrays = [
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
        ]

        square_hashmap_arrays = [
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0},
            {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
        ]

        for row_index in range(len(board)):
            square_row_index = row_index // 3
            row_array = board[row_index]
            row_hashmap = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
            
            for column_index in range(len(row_array)):
                square_value = row_array[column_index]
                if square_value != ".":
                    row_hashmap[square_value] += 1

                    #Row contains duplicate, return false
                    if row_hashmap[square_value] > 1:
                        return False

                    #Now add them to column hashmaps
                    specific_column_tracker_hashmap = column_hashmap_arrays[column_index]
                    specific_column_tracker_hashmap[square_value] += 1

                    if specific_column_tracker_hashmap[square_value] > 1:
                        return False

                    #Now add them to square hashmaps
                    square_column_index = column_index // 3
                    
                    #Find which square box it is - each square box has an index left to right
                    box_index = square_row_index * 3 + square_column_index
                    specific_square_tracker_hashmap = square_hashmap_arrays[box_index]
                    specific_square_tracker_hashmap[square_value] += 1

                    if specific_square_tracker_hashmap[square_value] > 1:
                        return False

        return True
