# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis
* --:--:-- in the time slot means that I couldn't solve it on my own

## Stack Problems

### #20 Valid Parentheses
⌛14:18:66 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(n)**, **O(1)**
  * **IDEA**: Use a stack to match openers to closers
  * **ALGORITHM**:
    1. Create a stack using the `deque` object of the `collections` library
    2. Create a set each for all possible openers and all possible closers
    3. Create a dictionary to match closers to openers
       <br>**NOTE**: The order here is important to ensure that checking for matches stays an O(1) operation
    4. For each character in s:
       1. If the character is an opener, push it onto the stack
       2. If the character is an opener:
          1. If the stack is NOT empty and the top element is the matching opener of the character, pop the top element
          2. Else, push the character onto the stack
    5. Return whether the stack is empty of not
* Solution Approach: → **O(n)**, **O(1)**
  * **IDEA**: Same as Initial Approach but without the opener and closer sets (uses the dictionary `.keys()` and `.values()` functions instead)
  <br>**NOTE**: We already knew that we could check if a character was in keys in O(1) time; the issue was checking if a character was in values. Typically, this would be an O(n) operation. However, because we have a fixed number of values, the time complexity is O(3), which is O(1), allowing us to maintain the O(1) runtime to check the dictionary's values.
  * Improvements:
    1. Less space used

**THOUGHTS**: Given how familiar I am with this problem, I am ashamed of how long it took me to solve it. It also reduces my confidence in stack and queue questions, data structures with which I belived myself to be comfortable. 

### #71 Simplify Path
⌛11:56:78 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(n)**, **O(1)**
  * **IDEA**: Iterate through the string and use a stack to pop elements based on if we've reached the parent character, ".."
  * **ALGORITHM**:
    1. Create stack to store path components
    2. Get path component parts using the `split()` inbuilt Python function
    3. For part in parts:
       1. If we reach the current character, '.', or an empty part, continue to the next iteration
       2. Else if we reach the parent character, '..' and the stack is not empty, pop the current top from the stack
       3. Else, push the part onto the stack
      <br>**NOTE**: We are told that the only possible characters are characters are alphanumeric, '.', '/' and '_'. We split the path into parts by '/' and both '_' and '...' can be considered part of the path name.
    4. Return "/" + a join of the current stack elements
    <br>**NOTE**: The path always starts with a slash, which is why there is a '/' before the join()
* Solution Approach:
  * **IDEA**: Same as Initial Approach but removed the unnecessary conditional in the return statement

**NOTE**: You can get empty strings in the resulting array when using the `split()` operation if there is no other character between the delimiter and the next delimeter (or if the delimiter is at the beginning or end) e.g.
<br> &nbsp; &nbsp; &nbsp; `split("/home")` >> `["", "home", ""]`
<br> &nbsp; &nbsp; &nbsp; `split("/home//foo/")` >> `["", "home", "", "foo", ""]`

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/