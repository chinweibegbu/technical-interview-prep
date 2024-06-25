# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis
* --:--:-- in the time slot means that I couldn't solve it on my own

## Matrix Problems

### #36 Valid Sudoku
⌛43:06:55 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(i<sup>3</sup>)**, **O(i<sup>2</sup>)**
  * **IDEA**: For each cell, check that its value is valid within its row, column and box
  * **ALGORITHM**: See comments of `isValidSudoku_initial()` function in `./matrix_36.py`
* Solution Approach: Same as Initial Approach but different implementation for the checking of rows, columns and boxes
* Optimal Approach: → **O(i<sup>3</sup>)**, **O(i<sup>2</sup>)**
  * [Solution by julialokot](https://leetcode.com/problems/valid-sudoku/solutions/3277043/beats-96-78-short-7-line-python-solution-with-detailed-explanation)
  * **IDEA**: Check that there is only one of each element-row, element-column and element-box pairing using the `set()` operation
  * **ALGORITHM**: See comments of `isValidSudoku_optimal()` function in `./matrix_36.py` 

**THOUGHTS**: julialokot's solution is so f***ing genius to me, wow.

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/