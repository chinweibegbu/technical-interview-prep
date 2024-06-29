from typing import List

def spiralOrder_initial_FAILED(matrix: List[List[int]]) -> List[int]:
    cur = [0,0]
    is_j = increasing = True  
            
    output = []
    m, n = len(matrix), len(matrix[0])

    # The two variables below track how far into the spiral we are
    spiraller = 0
    changes = 0

    for i in range(m*n):
        output.append(matrix[cur[0]][cur[1]])

        if (is_j and increasing):
            if (cur[1] + 1) >= (n - spiraller):
                is_j = False
                cur[0] += 1
                changes += 1   
            else:   
                cur[1] += 1
        elif (is_j and (not increasing)):
            if (cur[1] - 1) < (0 + spiraller):
                is_j = False
                cur[0] -= 1
                changes += 1   
            else:   
                cur[1] -= 1
        elif ((not is_j) and increasing):
            if (cur[0] + 1) >= (m - spiraller):
                is_j = True
                increasing = False
                cur[1] -= 1
                changes += 1   
            else:   
                cur[0] += 1
        else:
            if (cur[0] - 1) < (0 + spiraller):
                is_j = True
                increasing = True
                cur[1] += 1
                changes += 1   
            else:   
                cur[0] -= 1    

        if (changes == 3):
            spiraller += 1
            changes = 1   
    
    return output

# Based on https://youtu.be/BJnMZNwUk1M
def spiralOrder_optimal(matrix: List[List[int]]) -> List[int]:
    pass