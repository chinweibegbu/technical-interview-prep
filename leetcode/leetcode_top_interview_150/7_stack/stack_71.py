from collections import deque

def simplifyPath_initial(path: str) -> str:
    stack = deque([])
    # Get path component parts
    parts = path.split('/')

    for part in parts:
        if (part == '.' or part == ''):
            continue
        elif (part == '..'):
            if stack:
                stack.pop()
        else:
            stack.append(part)
    
    # Get the simplified path elements
    return "/" + ("/".join(list(stack)) if stack else "")

def simplifyPath_solution(path: str) -> str:
    # Create stack to store path components
    stack = deque([])

    # Get path component parts
    parts = path.split('/')
    
    # For part in parts:
    for part in parts:
        # If we reach the current character, '.', or an empty part, skip
        if (part == '.' or part == ''):
            continue
        # If we reach the parent character, '..' and the stack is not empty, pop
        elif (part == '..'):
            if stack:
                stack.pop()
        # If we reach any other part type, push it onto the stack
        else:
            stack.append(part)
    
    # Get the simplified path elements and join them with a '/' delimiter
    return "/" + "/".join(list(stack))
