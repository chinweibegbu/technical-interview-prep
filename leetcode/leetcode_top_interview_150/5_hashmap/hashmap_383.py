from collections import Counter

def canConstruct_solution(ransomNote: str, magazine: str) -> bool:
    # Get character counts for both inputs
    letters_r = {}
    letters_m = {}
    for r in ransomNote:
        letters_r[r] = letters_r.get(r, 0) + 1
    for m in magazine:
        letters_m[m] = letters_m.get(m, 0) + 1
    
    # For each unique letter in the ransom note...
    for letter_r in letters_r.keys():
        # ... If the count for that letter is less in the magazine, return False
        if (letters_m.get(letter_r, 0) < letters_r[letter_r]):
            return False

    # If the magazine has enough of every letter to make the ransom note, return True
    return True

def canConstruct_optimal(ransomNote: str, magazine: str) -> bool:
    # Get character counts for both inputs
    letters_r = Counter(ransomNote)
    letters_m = Counter(magazine)
    
    # For each unique letter in the ransom note...
    for letter_r in letters_r.keys():
        # ... If the count for that letter is less in the magazine, return False
        if (letters_m.get(letter_r, 0) < letters_r[letter_r]):
            return False

    # If the magazine has enough of every letter to make the ransom note, return True
    return True