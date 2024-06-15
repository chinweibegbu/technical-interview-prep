def strStr_solution(haystack: str, needle: str) -> int:
    return haystack.find(needle)

def strStr_optimal(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if (haystack[i : i+len(needle)] == needle):
            return i
    return -1