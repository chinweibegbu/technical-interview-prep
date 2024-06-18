from typing import List

def canCompleteCircuit_initial_FAILED(gas: List[int], cost: List[int]) -> int:
    if (len(gas) == 1):
        return 0 if (gas[0] >= cost[0]) else -1

    numStations = len(gas)
    tank = 0
    counter = 0

    # For each station in the circuit:
    for start in range(numStations):
        # Add initial gas to tank
        tank += gas[start]

        # For each possible position in the circuit:
        for cur in range(start, start+(numStations)+1):
            # If we have circled the block, return the current station (start)
            if (counter == numStations):
                return start
            # Else:
            else:
                # If tank >= cost, subtract cost and add the new position's gas to the tank
                if (tank >= cost[(cur % numStations)]):
                    tank -= cost[(cur % numStations)]
                    tank += gas[(((cur+1) % numStations))]
                    counter += 1
                # Else, reset, break and try a different station as a starting point
                else:
                    tank = 0
                    counter = 0
                    break
            
    # If you reach here, Return -1
    return -1

# Code from https://youtu.be/lJwbPZGo05A
def canCompleteCircuit_optimal(gas: List[int], cost: List[int]) -> int:
    
    if (sum(gas) < sum(cost)):
        return -1
    
    start, total = 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i+1
            total = 0
    
    return start