from typing import List    

# This code never worked BUT it had the exact same idea as Neetcode's, which is why I thought to include it
def fullJustify_intial_FAILED(words: List[str], maxWidth: int) -> List[str]:
    
    letterTotal = 0
    start, end = 0, 0
    result = []

    for i in range(len(words)):
        # If we are at the end of the array, create a line with the words remaining in left-justified manner
        if (i == len(words)-1):
            lineWords = words[start:end+1]
            line = ""
            for j in range(len(lineWords) - 1):
                line += lineWords[j] + " "
            rightPadding = " " * (maxWidth - len(line) + len(lineWords[-1]))
            line += lineWords[len(lineWords)-1] + rightPadding
            result.append(line)
        # If the length of the word added to lineLength + the minimum number of spaces is greater than the maxwidth, create a line with the words in the start and end index 
        elif (letterTotal + len(words[i]) + (end-start)) > maxWidth:
            print("-----creating line with words {}".format(words[start:end+1]))
            lineWords = words[start:end+1]
            lengths = [len(w) for w in lineWords]
            padding = " " * ((maxWidth - sum(lengths)) // max(1, end-start))
            line = ""
            for j in range(len(lineWords) - 1):
                line += lineWords[j] + padding
            line += lineWords[len(lineWords)-1]
            print(line)
            result.append(line)
            
            letterTotal = len(words[i])
            start = i
            end = i
        # If we have not exceeded maxWidth, add the current word and increment the pointer to the end of the line
        elif (letterTotal + len(words[i]) + (end-start)) <= maxWidth:
            letterTotal += len(words[i])
            end = i

        print("i: {} || start: {} || end: {} || letterTotal: {}".format(i, start, end, letterTotal))
    
    return result

# Code from https://youtu.be/TzMl4Z7pVh8
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    res = []
    line, length = [], 0
    i = 0
    while i < len(words):
        if length + len(line) + len(words[i]) > maxWidth:
            # Line complete
            extra_space = maxWidth - length
            spaces = extra_space // max(1, len(line) - 1)
            remainder = extra_space % max(1, len(line) -1)
            
            for j in range(max(1, len(line) - 1)):
                line[j] += " " * spaces
                if remainder:
                    line[j] += " "
                    remainder -= 1
            res.append("".join(line))
            line, length = [], 0 # Reset line and length
            
    line.append(words[i])
    length += len(words[i])
    i += 1
    
    # Handling last line
    last_line = " ".join(line)
    trail_space = maxWidth - len (last_line)
    res.append(last_line + " " * trail_space)
    return res    
    