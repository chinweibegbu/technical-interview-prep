from typing import List
def isValidSudoku_initial(board: List[List[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            # Get the current cell
            cell = board[i][j]

            # Skip empty cells
            if (cell == "."):
                continue
            
            # For each cell in the current row, check that the current cell only occurs once
            count = 0
            for r in board[i]:
                if cell == r:
                    count += 1
                # If the current cell occurs more than once, return False
                if count > 1:
                    return False

            # For each cell in the current column, check that the current cell only occurs once                
            count = 0
            for c in [[x, j] for x in range(9)]:
                if cell == board[c[0]][c[1]]:
                    count += 1
                # If the current cell occurs more than once, return False
                if count > 1:
                    return False

            # Get the current box
            box_i, box_j = i//3, j//3
            range_i_start, range_i_end = (box_i)*3, (box_i+1)*3
            range_j_start, range_j_end = (box_j)*3, (box_j+1)*3
            box = [[x,y] for x in range(range_i_start, range_i_end) 
            # For each cell in the current box, check that the current cell only occurs once
            for y in range(range_j_start, range_j_end)]
            count = 0
            for b in box:
                if cell == board[b[0]][b[1]]:
                    count += 1
                # If the current cell occurs more than once, return False
                if count > 1:
                    return False

    # Return True if every cell is valid within its row, column and box
    return True

def isValidSudoku_solution(board: List[List[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            # Get the current cell
            cell = board[i][j]

            # Skip empty cells
            if (cell == "."):
                continue
            
            # For each cell in the current row, check that the current cell does not occur anywhere else
            for r in [[i, x] for x in range(9)]:
                if ((cell == board[r[0]][r[1]]) and ([i, j] != r)):
                    return False

            # For each cell in the current column, check that the current cell does not occur anywhere else        
            for c in [[x, j] for x in range(9)]:
                if ((cell == board[c[0]][c[1]]) and ([i, j] != c)):
                    return False

            # Get the current box
            box_i, box_j = i//3, j//3
            range_i_start, range_i_end = (box_i)*3, (box_i+1)*3
            range_j_start, range_j_end = (box_j)*3, (box_j+1)*3
            box = [[x,y] for x in range(range_i_start, range_i_end) for y in range(range_j_start, range_j_end)] 
            # For each cell in the current box, check that the current cell does not occur anywhere else
            for b in box:
                if ((cell == board[b[0]][b[1]]) and ([i, j] != b)):
                    return False

    # Return True if every cell is valid within its row, column and box
    return True

def isValidSudoku_optimal(board: List[List[str]]) -> bool:
    # Use an array to store all non-empty elements on the board
    res = []
    
    # Loop through each row
    for i in range(9):
        # Loop through each column
        for j in range(9):
            # Get the current element 
            element = board[i][j]
            
            # For non-empty elements only...
            if element != '.':
                # Add an array with three tuples:
                # 1. The element and its row index
                # 2. The element and its column index
                # 3. The element and its box indices
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    
    # Check that there are no repititions using the set operation
    return len(res) == len(set(res))