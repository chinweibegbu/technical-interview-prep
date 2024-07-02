from collections import deque

def isValid(s: str) -> bool:
    stack = deque([])
    match = { "}": "{", ")": "(", "]": "["}

    for char in s:
        # If char is an opener, push char onto the stack
        if (char in match.values()):
            stack.append(char)
        # If char is a closer...
        if (char in match.keys()):
            # ... And the top element matches it, pop said element
            if (len(stack) > 0) and (match[char] == stack[-1]):
                stack.pop()
            # ... And there is no top element OR they do not match, push char onto the stack
            else:
                stack.append(char)
        
    # The parentheses are valid if the stack is empty by the end of iteration
    return (len(stack) == 0)
