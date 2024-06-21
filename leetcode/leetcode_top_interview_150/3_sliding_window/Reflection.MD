# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis
* --:--:-- in the time slot means that I couldn't solve it on my own

## Sliding Window Problems

### #209 Minimum Size Subarray Sum
⌛--:--:-- &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach #1 (FaILED): → **O(n <sup>2</sup>)**, **O(1)**
  * **IDEA**: Brute force >>> Check the sum for every possible subarray for every possible length of the window
  * Failed because it exceeded the time limit
* Initial Approach #2 (FAILED): → **O(n <sup>2</sup>)**, **O(1)**
  * **IDEA**: Start from both extremes of the array and move in based on the sum of the array when you move the left vs the right pointer inwards
  * Failed because it exceeded the time limit (specifically because it calculated the sum, an O(n) operation on each iteration)
* Optimal Approach: → **O(n)**, **O(1)**
  * Based on understanding of [Neetcode's explanation, NOT code](https://youtu.be/aYqYMIqZx5s)
  * **IDEA**: Iterate through the array with two pointers initiated at the beginning. Shift the right pointer when the current total is not up to the target and the left pointer when it is.
  * **ALGORITHM**:
    1. Initialise left and right pointers, l and r, to 0
    2. Initialise the minimum length to 1 greater than n (OR +ve infinity)
    3. Initialise the total to the first element in the array
    4. While l is less than r AND r is less than n:
       1. If the total is less than the target, increment r by 1 then add the value at the new r to the total (IF the new r is less than n)
       2. Else, we've reached a valid subarray:
          1. Replace the minimum with the length of the current subarray (r - l + 1) if it is less than what is currently stored there
          2. Subtract the value at l from the total
          3. Increment l by 1
    5. Return the minimum IF it has changed from it's initial value ELSE return 0

**THOUGHTS**: I want to practice more sliding window problems. 

### #3 Longest Substring Without Repeating Characters
⌛43:06:67 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: Initialise two pointers to the beginning of the string and track the characters that have occured. Extend the window on the right until a character is repeated is found, in which case, shrink the window on the left until the character that was repeated is found.
  * **ALGORITHM**: See `./sliding_window_3.py` numbered comments

**NOTE**: Remember to consider edge cases

### #88 Substring with Concatenation of All Words
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(n)**, **O(1)**
  * 
* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: 
  * **ALGORITHM**:
    1. 
  * Improvements:
    1. 
* Optimal Approach: → **O(n)**, **O(1)**
  * 

**THOUGHTS**: 

**NOTE**: 

### #88 Minimum Window Substring
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(n)**, **O(1)**
  * 
* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: 
  * **ALGORITHM**:
    1. 
  * Improvements:
    1. 
* Optimal Approach: → **O(n)**, **O(1)**
  * 

**THOUGHTS**: 

**NOTE**: 


## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/