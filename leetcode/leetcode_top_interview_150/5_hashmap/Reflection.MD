# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis
* --:--:-- in the time slot means that I couldn't solve it on my own

## Sorting Algorithm Problems

### #383 Ransome Note
⌛07:13:08 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150)

> r: length of ransom note
> m: length of magazine

* Solution Approach: → **O(r+m)**, **O(1)**
  * **IDEA**: Create dictionaries of both then compare the counts for each letter in the ransom note
  * **ALGORITHM**: See comments in `./hashmap_383.py`
* Optimal Approach: → **O(n)**, **O(1)**
  * Based on [Solution by Sajal_](https://leetcode.com/problems/ransom-note/solutions/5156605/one-liner-easy-way)
  * **IDEA**: Use the `Counter` object from the Python `collections` library to count the number of character occurences in both inputs

**NOTE**: 
* You can perform arithmetic operations e.g. `-` and `+` on `Counter` objects (see [Solution by Sajal_](https://leetcode.com/problems/ransom-note/solutions/5156605/one-liner-easy-way))
* There is a `count()` function for strings in Python

### #205 Isomorphic Strings
⌛21:56:39 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150)

> s: length of string s
> t: length of string t

* Initial Approach: → **O(s*t)**, **O(s+t)**
  * **IDEA**: Save all unique characters and where they occur in both strings then check that those indices occur in both.
  * See comments in `./hashmap_205.py`
* Solution Approach: → **O(s*t)**, **O(s+t)**
  * **IDEA**: Same as Initial Approach but used the `enumerate()` function to get access to both current index and character with an in-built Python function
* ### #205 Isomorphic Strings
⌛21:56:39 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150)

> s: length of string s
> t: length of string t

* Initial Approach: → **O(s*t)**, **O(s+t)**
  * **IDEA**: Save all unique characters and where they occur in both strings then check that those indices occur in both.
  * See comments in `./hashmap_205.py`
* Solution Approach: → **O(s*t)**, **O(s+t)**
  * **IDEA**: Same as Initial Approach but used the `enumerate()` function to get access to both current index and character with an in-built Python function

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/