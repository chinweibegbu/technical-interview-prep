def reverseWords_solution(s: str) -> str:
    reversed_ver = s.split()[::-1]
    result = ""
    for i in range(len(reversed_ver)):
        result += reversed_ver[i]
        if (i != len(reversed_ver)-1):
            result += " "
    return result


def reverseWords_optimal(s: str) -> str:
    return " ".join(s.split()[::-1])