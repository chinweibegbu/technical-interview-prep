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

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/