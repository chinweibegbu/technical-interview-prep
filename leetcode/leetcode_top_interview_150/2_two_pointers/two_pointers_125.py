def isPalindrome_solution(s: str) -> bool:
    valid_characters = {x:1 for x in "abcdefghijklmnopqrstuvwxyz0123456789"}
    chars = [c for c in list(s.lower()) if c in valid_characters]

    l, r = 0, len(chars)-1
    while l <= r:
        if (chars[l] != chars[r]):
            return False
        l += 1
        r -= 1
    
    return True

def isPalindrome_optimal(s: str) -> bool:
    chars = [c for c in s.lower() if c.isalnum()]

    l, r = 0, len(chars)-1
    while l <= r:
        if (chars[l] != chars[r]):
            return False
        l += 1
        r -= 1
    
    return True
