def wordPattern(self, pattern: str, s: str) -> bool:
    # Edge case: Pattern and string are NOT the same length
    if len(pattern) != len(s.split()): return False

    mapper = {}
    for cur, word in zip(pattern, s.split()):
        # If the current pattern char is not in the mapper...
        if cur not in mapper:
            # If the current word is in the mapper, return False
            if word in mapper.values():
                return False
            # Else, assign the current pattern char key the value of the current word 
            mapper[cur] = word
        # If the current pattern char is in the mapper but the value does not match, return False
        else:
            if (mapper[cur] != word):
                return False
    
    # Return True if every pattern character and word match
    return True