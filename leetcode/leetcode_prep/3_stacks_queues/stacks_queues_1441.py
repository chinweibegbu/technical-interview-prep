from collections import List, deque

def buildArray(self, target: List[int], n: int) -> List[str]:
    # Initialise stack (use pop() and append()) and return list
    stack = deque()
    operations = []

    # Track current target a.k.a. target[index]
    index = 0
    for x in range(1,n+1):
        # Add x to stack and note operations
        stack.append(x)
        operations.append("Push")

        # If the element does not match the current target, pop()
        if (x != target[index]):
            stack.pop()
            operations.append("Pop")
        # Else, increment index
        else:
            index += 1
        
        # Break if the target array has been constructed
        if (len(stack) == len(target)):
            break
    
    # Return the list of operations
    return operations