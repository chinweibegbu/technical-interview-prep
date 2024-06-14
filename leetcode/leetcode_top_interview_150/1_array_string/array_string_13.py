def romanToInt(s: str) -> int:
    # Use a dictionary to map roman numerals to decimal integers
    trans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    cur, nex = [0, 0], 1
    
    # Continue until the word is complete
    while (cur[0] < len(s)):
        # If you've reached the last character or pair of characters...
        if (nex >= len(s)):
            # ... and there are two characters, translate with that in mind
            if (cur[0] != cur[1]):
                total += (trans[s[cur[1]]] - trans[s[cur[0]]])
                cur[0] += 2
            # ... or there is one character, translate with that in mind
            else:
                total += trans[s[cur[0]]]
                cur[0] += 1
                
        # If the current character or pair of characters is larger than what follows...
        elif (trans[s[cur[1]]] >= trans[s[nex]]):
            # ... and there are two characters, translate with that in mind
            if (cur[0] != cur[1]):
                total += (trans[s[cur[1]]] - trans[s[cur[0]]])
                cur[0] += 2
            # ... or there is one character, translate with that in mind
            else:
                total += trans[s[cur[0]]]
                cur[0] += 1
        
        # Update the second current pointer and next pointer regardless of the case
        cur[1] += 1
        nex += 1

    # Return the total value of the provided string
    return total
