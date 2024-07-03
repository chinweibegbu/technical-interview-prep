from collections import deque

def calculate_initial_FAILED(s: str) -> int:
    # Remove spaces -> O(n)
    s = "".join(s.split())

    # Evaluate expressions
    operands = deque([])
    operators = deque([])

    # For token in s... -> O(n)
    for i, token in enumerate(s):
        # Skip brackets
        if token in ["(", ")"]:
            continue
        # Note operators
        elif token in ["+", "-"]:
            operators.append(token)
        # Evaluate or push with operands
        else:
            if (i == 0) or ((s[i-1]) not in ["+", "-"]):
                operands.append(int(token))
            elif ((operators[-1]) in ["+", "-"]):
                operand_1 = operands.pop()
                operand_2 = int(token)
                operator = operators.pop()
                if operator == "+":
                    operands.append(operand_1 + operand_2)
                else:
                    operands.append(operand_1 - operand_2)

    # While there are operators remaining, evaluate
    while (operators):
        operand_2 = operands.pop()
        operand_1 = operands.pop()
        operator = operators.pop()
        if operator == "+":
            operands.append(operand_1 + operand_2)
        else:
            operands.append(operand_1 - operand_2)

    # Return the current top of the array
    return operands[-1]