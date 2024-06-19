def isSubsequence_initial(s: str, t: str) -> bool:
    # Edge case: If t is empty while s is not, return False
    if ((not t) and s):
        return False

    sp, tp = 0, 0

    while (sp < len(s)):
        # If we reach the end of t before the end of t, not all characters in s are in t in the right order
        if (tp >= len(t)):
            return False
        
        # If we found the current s character in t, move to the next s character
        if (s[sp] == t[tp]):
            sp += 1
        
        # Increment t whether they are the same or not
        tp += 1
    
    return True

def isSubsequence_solution(s: str, t: str) -> bool:
    sp, tp = 0, 0

    while (sp < len(s)):
        if (tp >= len(t)):
            return False
        
        if (s[sp] == t[tp]):
            sp += 1
        tp += 1
    
    return True
