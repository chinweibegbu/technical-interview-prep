from collections import deque
from typing import List

def evalRPN_solution(tokens: List[str]) -> int:
    stack = deque([])
    operators = set(["+", "-", "*", "/"])
    for token in tokens:
        if token in operators:
            # Pop in the order of operands
            b = stack.pop()
            a = stack.pop()
            if (token == "+"):
                stack.append(a+b)
            elif (token == "-"):
                stack.append(a-b)
            elif (token == "*"):
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        else:
            stack.append(int(token))

    return stack[-1]