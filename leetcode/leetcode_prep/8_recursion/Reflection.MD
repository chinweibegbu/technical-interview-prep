# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Recursion Problems

### #201 Power of Two
⌛12:00:49 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/power-of-two/)

* Solution Approach: {RECURSIVE} → **O(log n)**, **O(n)**
  * n is a power of 2 if it can be divided by 2 until it reaches 1
  * Edge cases:
    * If n is less than or equal to 0, return false
  * RECURSIVE APPROACH:
    * Base case: If cur is 1, return true
    * General case: If cur is evenly divisible by 2, call recursively on cur/2. Else, return False
* Alternative Approaches: 
  * Return true if n is greater than 0 and its binary representation has exactly one 1. → **O(log n)**, **O(1)**
  <br>**NOTE**: This made me realise how small my outlook is. There are so many angles from which I can look at the problem. I can use information from seemingly unrelated concepts. Interesting.

  * Return true if there exists a number x in range 0 to 31 that n is equal to such that 2^x is n. → **O(1)**, **O(1)**
  <br>**NOTE**: This made me realise how I had really neglected the constraints of the problem. By using the constraints of the problem, the user was able to reduce runtime complexity to O(1). Funnily enough, I had the same idea but I was wondering when I would stop incrementing x so I gave up on it - the answer to my question was in the constraint.

### #226 Power of Three
⌛02:10:25 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/power-of-three/)

* Solution Approach: {RECURSIVE} → **O(log n)**, **O(n)**
  * n is a power of 3 if it can be divided by 3 until it reaches 1
  * Edge cases:
    * If n is less than or equal to 0, return false
  * RECURSIVE APPROACH:
    * Base case: If cur is 1, return true
    * General case: If cur is evenly divisible by 3, call recursively on cur/3. Else, return False

**NOTE**: On this question, I streamlined the code from #201.

### #342 Power of Four
⌛06:56:44 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/power-of-four/)

* Initial Approaches:
  1. If n is less than or equal to 0. Return true if there exists a number x in range 0 to 31 that n is equal to such that 2^x is n AND x is divisible by 2. Return false if you get out of this loop without returning. → **O(1)**, **O(1)**
  <br>**NOTE**: This approach was based on the fact that **4<sup>x</sup>** is equal to **2<sup>2x</sup>** and it had the same constraints as #201.
  2. Same as Initial Approach #1 but remove the conditional at the beginning and the `return False` at the end → **O(1)**, **O(1)**
  <br>**NOTE**: The reasons for doing this are:
      - The function addresses the edge case eventually so there is no need (??) to create a separate conditional to deal with it
      - The function returns false by default so there is no need tell it to return false at the end
* Solution approach: Same as Initial Approach #2 but only checks if x is divisible by 2 if it is already known that 2<sup>x</sup> is equal to n → **O(1)**, **O(1)**
* Alternative approach: Recursive approach → **O(log<sub>4</sub> n)**, **O(n)**
  
### #509 Fibonacci Number
⌛06:56:44 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/fibonacci-number/)

* Solution Approach: → **O(n)**, **O(n)**
  * If n is less than 2, return n
  * Else, return the recursed call on `n-1` and `n-2`
* Optimal approach: Same as initial approach but use a cache which already has the results for `fib(0)` and `fib(1)` in it
  <br>**NOTE**: The point of the cache is to share information between calls of the function e.g. when you call `fib(5)`, store all the results of `fib()` calls from 2 to 5 such that, when you call `fib(7)`, the recursive stack shortens.

### #21 Merge Two Sorted Lists
⌛18:23:77 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-two-sorted-lists/)

* Initial Approach #1: → **O(n)**, **O(n)**
  * If both lists are empty, return either; Else if one list and the other isn't, return the other
  * Else,
    * Create a new head based on the lesser of both lists' heads
    * Create a tail to make entry O(1)
    * While both lists' pointers are not null, add the lesser of the two current vals to the new list and update the "winner" list and the new list pointer
    * Return the new list's head
* Initial Approach #2: → **O(n)**, **O(n)**
  * If both lists are empty, return either; Else if one list and the other isn't, return the other
  * Else,
    * Create a new list
    * While both lists' pointers are not null, add the lesser of the two current vals to the new list and update the "winner" list and the new list pointer
    * Return the new list's head's next
* Optimal approach: Same as Initial Approach #2, but remove the conditional at the beginning, as the code in the final else block covers all cases. → **O(n)**, **O(n)**

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/