def convert_solution(s: str, numRows: int) -> str:
    # Edge Case: 1 row of zig zags OR 1 letter
    if (numRows == 1) or (len(s) == 1): return s

    # Keep track of each rows content in an array of strings where arr[i] = content of row i
    rows = [""]*numRows

    # Handle the first letter of the word...
    # ... By adding it to the first row and setting rowIndex to 1
    rows[0] = s[0]
    rowIndex = 1

    # Start adding to the rows in increasing order
    direction = True

    # Continue until the end of the string
    for i in range(1, len(s)):
        # Add the current character to the appropiate row
        rows[rowIndex] += s[i]

        # Swap the direction if we've gotten to the first or last row
        if ((rowIndex == numRows-1) or (rowIndex == 0)):
            direction = not direction

        # Update rowIndex
        rowIndex += 1 if direction else -1
    
    # Return the combination of the rows (in order)
    return ''.join(rows)