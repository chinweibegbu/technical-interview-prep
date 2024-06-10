# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Sorting Algorithm Problems

### #88 Merge Sorted Array
⌛47:57:45 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(n+m)**, **O(n+m)**
  * **IDEA**: Use pointers and a temp array.
  * Edge case:
    * If nums2 is empty, don't do anything else
    * If nums1 is empty, move everthing in nums2 to nums1 and don't do anything else
  * **ALGORITHM**:
    1. Have pointers i and j to the beginnings of nums1 and nums2, respectively
    2. If nums1[i] is less than nums2[j], append nums1[i] to the temp array and increment i by 1
    3. Else, append nums2[j] to the temp array and increment j by 1
    4. Continue until either all the elements in nums1 or nums2 has been accounted for
    5. Add the remaining elements in nums1 or nums2 (if they exist) to the temp array
    6. Reassign nums1 to the temp array
* Solution Approach: → **O(n+m)**, **O(1)**
  * **IDEA**: Use pointers but start from the back of nums1 so you don't need a temp array
  * **ALGORITHM**:
    1. Have pointers i, j and k to point to the end of nums1 elements, nums2 and nums1, respectively
    2. If nums1[i] is greater than nums2[j], assign nums1[k] to nums1[i] and decrement i by 1
    3. Else, assign nums1[k] to nums1[i] and decrement i by 1
    4. Continue until either all the elements in nums1 or nums2 has been accounted for
    5. Add the elements remaining at the beginning nums2 to the beginning of nums1 (if they exist)

**THOUGHTS**: Wow this took so long, I am so so very afraid of how long things are going to take me if an Easy array question took me this long. Not a good start.

**NOTE**: Always, always step through the code with a sample case.

### #88 Remove Element
⌛51:21:63 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach:
  * 
* Solution Approach: → **O(n logn)**, **O(n)**
  * **IDEA**: 
  * **ALGORITHM**:
    1. 
  * Improvements:
    1. 
* Optimal Approach: 
  * 

**THOUGHTS**: No f***ing way, bro. The time stamps for these FIRST two ARRAY questions has me wondering at my general capability. 

**NOTE**: Do a better job with identifying and stepping through code with edge cases.

### #26 Remove Duplicates from Sorted Array
⌛17:12:93 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(1)**
  * **IDEA**: Use pointers to keep track of unique elements in the front of the array with non-unique elements swapped to the back
  * **ALGORITHM**:
    1. EDGE CASE: If the arrray has less than two elements, return the length of the array (an empty array has no unique elements and an array with one element has one unique element)
    2. Initialise pointers to the last index of the unique sub-array (first element i.e. index 0) and a parser pointer to the first element we are unsure is unique (second element i.e. index 1)
    3. While the parser has not exceeded the length of the array:
       1. If the last unique element and the current element are not the same, swap the current element with the element IN FRONT of the last unique element then increment the unique pointer
       2. Increment the parser pointer
    4. Return the index of the last unique element + 1

**THOUGHTS**: I have solved this before and I solved it a lot faster than the first time (see `../../leetcode_prep/1_arrays/arrays_26.py`). I learned from the lessons of the first two by making sure to step through the code and doing the same for edge cases I thought of. Good job, Chinwe.

### #88 Remove Duplicates from Sorted Array II
⌛48:45:57 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach: → **O(n)**, **O(1)**
  * **IDEA**: Use the same approach as with #26 but keep track of the number of times each unique element appears as well
  * **ALGORITHM**: Frankly, I created an algorithm based on my step-through and I am finding it hard to describe it. Just see `removeDuplicates_initial()`./arrays_80.py`
* Solution Approach: → **O(n)**, **O(1)**
  * **IDEA**: Initial approach, but remove the unnecessary swap
* Optimal Approach: 
  * [Solution by geekytaurus](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/4511964/easy-o-n-python-java-go-c-beginner-friendly)
  * **IDEA**: Move elements to the modified subarray (length represented by u) if there are 2 or less of the current element
  * **ALGORITHM**:
    1. Initialize length pointer (u) to 1 (for the first element) and current frequency (f) to 1
    2. Iterate through the array, starting from index 1 (use "cur" to refer to element)
    3. If the cur is equal its prev, increment f. Else, reset f to 1
    4. If f <= 2, update the item after the modified array (i.e. u+1) with cur and increment u
    5. Continue until the end of the array

**NOTE**: I modified the variable names in the optimal solution for my own understanding. Also. it took me a while to create an "IDEA" sentence for the optimal solution - the "IDEA" sentence should be able to capture the core behind the algorithm. It is not the steps you take but WHY you took them (wod wod wod).

### #169 Majority Element
⌛04:12:11 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n logn)**, **O(1)**
  * **IDEA**: Sort the list and return the middle element >>> We can be sure that it is the middle element because the question tells us to assume that the majority element exists, which means there is an element which occurs more than len(nums)/2 times.
* Optimal Approach: → **O(n logn)**, **O(n)**
  * **IDEA**: [Boyer-Moore Majority Vote Algorithm](https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/)
  * **ALGORITHM**:
    1. Initialise count and candidate to 0 and None respectively
    2. For each element in nums
       1. If count is 0, update candidate to be the current element
       2. Increment or decrement count by 1 based on if candidate and the current element match, respectively
       3. Return candidate

**THOUGHTS**: I have already researched this algorithm before. I wonder if there is a way to keep in mind common algorithms already created to deal with certain problems...

**NOTE**: IT IS NOT ALWAYS A GIVEN THAT A MAJORITY ELEMENT EXISTS. This is an incomplete version of the Boyer-Moore Majority Vote algorithm, used becuase we are told to assume is that the majority element exists. The complete algorithm, after taking the steps already outlines, then counts the number of occurences of the majority candidate. If the count is greater than (n//2), it is the majority element; else, the majority element does NOT exist.

### #189 Rotate Array
⌛11:54:66 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: Use a temporary array to hold the elements in the rotated order then move them back to the original array.
  * **ALGORITHM**:
    1. Get the minimum number of rotations needed
    2. EDGE CASE: If k is 0 or a multiple of n, return
    3. Copy the array in the rotated order to a temporary array
    4. Copy the elements back to the original array
* Optimal Approach: 
  * [Solution by SonuDutta](https://leetcode.com/problems/rotate-array/solutions/5189694/easy-python-solution)
  * **ALGORITHM**:
    1. Get the minimum number of rotations needed
    2. Reverse the entire array in-place
    3. Reverse the first k elements in place
    4. Reverse the remaining n-k elements in place
   
**THOUGHTS**: How did this person come up with this? How did it occur to them? That's what I don't get.

### #121 Best Time to Buy and Sell Stock
⌛13:34:50 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach (FAILED): → **O(n<sup>2</sup>)**, **O(n)**
  * **IDEA**: Brute force approach >>>  Get every possible combination of buy and sell days then select the max profit of these combinations
  * **ALGORITHM**:
    1. EDGE CASE: If there are less than 2 elements/days, return 0
    2. For each element/day (except the last one)
       1. calculate the maximum possible profit by getting the maximum potential sell day (potential sell day: any day after buy day) and subtracting the current element/day from it
       2. Add calculated profit to profits array if it is greater than 0; else (i.e. the maximum profit is actually a loss), add 0
    3. Return the maximum of the stored profits
  * Failed because it exceeded the time limit (9999ms) with very large arrays (stopped trying to solve @ 54:35:25)
* Optimal Approach #1: → **O(n)**, **O(1)**
  * [Modified Kadane's Algorithm](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
  * **ALGORITHM (original)**:
    1. Initialize the variables max_so_far = INT_MIN and max_ending_here = 0
    2. Run a for loop from 0 to N-1 and for each index i:
       1. Add the arr[i] to max_ending_here
       2. If  max_so_far is less than max_ending_here then update max_so_far  to max_ending_here
       3. If max_ending_here < 0 then update max_ending_here = 0
    3. Return max_so_far
  * **ALGORITHM (modified)**:
    1. Initialize the variables max_prof = INT_MIN and cur_prof = 0
    <br>**NOTE**: cur_prof always returns to a minimun of 0 because, if we make a loss, we note the profit as 0, NOT the loss... lost
    2. For each index in range 0 to n-2 (because the last element canot have a profit):
       1. Add profit at this index (i.e. maximum value in potential sell days minus today) to cur_prof
       2. If  max_prof is less than cur_prof then update max_prof to cur_prof
       3. If cur_prof < 0 then update cur_prof = 0
    3. Return max_prof
  * See [Solution by nayankumarjha2](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/4801758/2-steps-kadane-s-algorithm-brute-better-optimal-easy-video-explanation-in-hindi) for example implementation of a modified Kadane's algorithm
* Optimal Approach #2: → **O(n)**, **O(1)**
  * **IDEA**: Return the maximum profit of all minimum points of the graph
  * **ALGORITHM**:
    1. Initialise buy and sell days to day 0 and 1, respectively
    2. While there are valid sell days:
       1. If the buy day's price is greater than the sell day's price, update buy and sell date
       2. Else, set maxProfit to the larger of the buy and sell days (with valid relative prices) and update the sell day
       <br>**NOTE**: Updating the minimum stock price (a.k.a. valid buy day) with a new one will not necessarily change the maxProfit; it is possible to have a lowest stock price which will not have as much as a profit as a higher stock price did.

    3. Return maxProfit
  * Improvements:
    *  I understand the intuition behind this one.

**NOTE**:
* I need to look for videos on Kadane's algorithm and make sure I understand HOW it works. As at now, I am unable to create an "IDEA" sentence.
* I implemented optimal approach #2 (no relation to Kadane's Algorithm) on my own and I consider that my solution 
  
### #122 Best Time to Buy and Sell Stock II
⌛07:49:18 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(1)**
  * **IDEA**: Add each potential profit to a counter as you iterate in pairs
  * **ALGORITHM**:
    1. Initialise buy and sell days to day 0 and 1, respectively
    2. While there are possible sell days:
       1. If the buy day's value is less than the sell day's value, subtract them and add to the total variable
       2. Move buy and sell day indices forward by 1
    3. Return total variable

**THOUGHTS**: This is the second time I tried to solve this question. On my first attempt, I was entirely unsuccessful and stopped trying after 35+ minutes.

**NOTE**:
  * Draw out the thought process as direct as possible (this has to do with how I work through case studies; for this question, Neetcode draws out a graph).
  * This algorithm would NOT work well if I had to return the days on which to buy and sell

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/