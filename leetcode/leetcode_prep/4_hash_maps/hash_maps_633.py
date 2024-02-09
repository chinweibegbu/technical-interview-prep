from collections import List

def findRepeatedDnaSequences_Initial(self, s: str) -> List[str]:
    sequences = {}
    for i in range(len(s)):
        # Break out of loop when 10-letter sequences can no longer be found
        if (i+10 > len(s)):
            break
        # Get sequence
        sequence = s[i:i+10]
        # Add sequence to dictionary or update its value
        sequences[sequence] = sequences.get(sequence, 0) + 1
    # Get sequences that appear more than once and return it
    valid = []
    for key, value in sequences.items():
        if (value > 1):
            valid.append(key)
    return valid

def findRepeatedDnaSequences_Solution(self, s: str) -> List[str]:
    sequences = {}
    for i in range(len(s)):
        # Break out of loop when 10-letter sequences can no longer be found
        if (i+10 > len(s)):
            break
        # Get sequence
        sequence = s[i:i+10]
        # Add sequence to dictionary or update its value
        sequences[sequence] = sequences.get(sequence, 0) + 1
    # Return sequences that appear more than once with list comprehension
    return [key for key, value in sequences.items() if value > 1]

def findRepeatedDnaSequences_Optimal(self, s: str) -> List[str]:
    # Edge case: s is less than 10 characters long
    if (len(s) < 10): return []

    sequences = {}
    valid_sequences = set()
    for i in range(len(s)-9):
        # Get sequence
        sequence = s[i:i+10]
        # If in dictionary, add to set. Else, add to dictionary
        if (sequence in sequences):
            valid_sequences.add(sequence)
        else:
            sequences[sequence] = 1

    # Return valid sequences
    return valid_sequences