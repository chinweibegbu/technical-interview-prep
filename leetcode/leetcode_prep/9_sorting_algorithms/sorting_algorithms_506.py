from collections import List

class Solution_Initial:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a sorted version of score
        score_sorted = list(reversed(sorted(score)))
        
        # Create the answer array
        n = len(score)
        answer = [None]*n

        places = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }

        for i in range(n):
            # Find the position of the current score in the sorted array
            place_index = score_sorted.index(score[i])
            
            # Put its place (based on its position in the sorted array) in the answer array
            answer[i] = places[place_index] if place_index < 3 else str(place_index + 1)
        
        return answer

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a sorted version of score
        score_sorted = sorted(score)

        n = len(score)
        places = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for i in range(n):
            # Find the position of the current score in the sorted array
            place_index = n - score_sorted.index(score[i])
            
            # Put its place (based on its position in the sorted array) in the answer array
            score[i] = places[place_index-1] if place_index <= 3 else str(place_index)
        
        return score

class Solution_Optimal:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a dictionary with... dictionary comprehension (??) to store the indices of the scores in their original (unsorted state)
        indices = {score[i]:i for i in range(len(score))}
        
        # Create an array of length n to hold the results
        places = [""] * len(score)
        
        # Store a sorted AND reversed version of score in a new array
        sort = sorted(score, reverse=True)

        """
        Breaking down below
        1. sort[i]: Get the current element in the sorted array
        2. htable[...]: Get the original index of the element in the unsorted array 
        3. rscores[...]: Assign place to original index in answer array
        """
        top_places = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(len(sort)):
            places[indices[sort[i]]] = top_places[i] if i < 3 else str(i+1)

        return places
