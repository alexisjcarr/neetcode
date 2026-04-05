class Solution:
    """
    explore:
        - each row has 1-9
        - each col has 1-9
        - each square has 1-9

    brainstorming:
        - sq idx: (row / 3) * 3 + (col / 3)
        - this will suck, but i think i need to do a dfs on row, col, and sq_idx
            - see if each value is in a temp set, if so: FALSE

    plan:
        rows, cols = 9, 9
        sq_idx_sets = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                if len([elem for elem in matrix[r] if elem.isnumeric()]) != len(set[...]):
                    return False

                if len([elem for elem in matrix[:][c] if elem.isnumeric()]) != len(set[...]):
                    return False

                sq_idx = (r / 3) * 3 + (c / 3)
                if matrix[r][c] in sq_idx_sets[sq_idx]:
                    return False

        return True

    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box_idx = (r // 3) * 3 + (c // 3)
                if (board[r][c].isnumeric() and 
                    (board[r][c] in row_set[r] or 
                    board[r][c] in col_set[c] or 
                    board[r][c] in box_set[box_idx])):
                        return False
                
                else:
                    row_set[r].add(board[r][c])
                    col_set[c].add(board[r][c])
                    box_set[box_idx].add(board[r][c])

        return True
   