from collections import defaultdict
from typing import List

def groupAnagrams_solution(strs: List[str]) -> List[List[str]]:
    tracker = {}
    for s in strs:
        # Sort the string 
        # WHY? Because anagrams will be the same string when they are sorted
        string = "".join(sorted(s))

        # Map sorted string to array of original words
        if not (string in tracker):
            tracker[string] = []
        tracker[string].append(s)

    # Return the values of the dictionary
    return list(tracker.values())
        
def groupAnagrams_optimal(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    return list(anagram_map.values())