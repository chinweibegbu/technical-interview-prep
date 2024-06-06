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

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/