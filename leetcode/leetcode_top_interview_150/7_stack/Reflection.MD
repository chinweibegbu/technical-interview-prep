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

### #155 Min Stack
⌛09:05:67 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(1)**, **O(n)**
  * **IDEA**: Keep two stacks - one for the elements and one for the minimum as at when the top element was pushed + Use the `deque` object from the `collections` library
  * **ALGORITHM**:
    * `push(val)`: Push val onto the main stack. If the minimum stack is empty OR val is smaller than its top, push val onto the minimum stack; else, push its top.
    * `pop()`: Pop from the main stack. Pop from the minimum stack. 
    * `top()`: Return the top of the main stack
    * `getMin()`: Return the top of the minimum stack.

### #150 Evaluate Reverse Polish Notation
⌛20:32:81 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: Store tokens in a stack and pop to evaluate when you reach an operator
  * **ALGORITHM**:
    1. Create a stack using the `deque` object of the `collections` library
    2. Create a set to store the operators and look them up in O(1) time
    <br>**NOTE**: In this question, an array could be used and still have O(1) runtime because we have a fixed number of operators (4).
    3. For token in tokens:
       1. If token in an operator:
          1. Pop from the stack twice
             <br>**NOTE**: The first popped element is the second operand while the second popped element is the first operand. This is important to note for subtraction and division, in which the order of operands matters.
          2. Push the result of the computation (based on the token operator) onto the stack
          <br>**NOTE**: I used an if confitional here but a `match-case` conditional can be used alternatively
       2. Else, push the integer version of the token onto the stack
    4. Return the top of the stack

**THOUGHTS**: I had no idea what "truncate towards 0" meant; that would have been explained in an interview context, I believe.


**NOTE:** To truncate is to discard the decimal portion of the result e.g. 3.8 rounded is 4.0 but 3.8 truncated is 3.0 (see an explanation on truncation vs rounding [here](https://www.ualberta.ca/computing-science/media-library/teaching-resources/java/truncation-rounding.html)). The `int()` operation around the result of dividing the operands truncated the result. 


### #88 Merge Sorted Array
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach (FAILED): → **O(n)**, **O(n)**
  * **IDEA**: Iterate through the string once, using stacks to keep track of the operands and operators
  * Failed because the idea did not consider every case, specifically:
    1. number with more than one digit
    2. -ve number or expression
  * Stopped trying at 48:12:91 with 8 out of 42 test cases passed
  <br>**THOUGHTS**: Abysmal but expected
  * Potential improvements based on understanding of Optimal Approach:
    * Ignore spaces when you encounter them rather than using the `strip()` operation on the entire string only one O(n) pass is needed
* Optimal Approach: → **O(n)**, **O(n)**
  * [Timothy H Chang's explanation and code](https://youtu.be/A3noAzWZ9f4)
  * **CODE**:
  ![Timothy H Chang's solution code for Leetcode #224](../images/timothy-h-chang_244_code.png)

**THOUGHTS**: Can you imagine that Neetcode didn't have a video for this problem? A first for me. 

**TODO**: Re-watch and implement on your own.

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/