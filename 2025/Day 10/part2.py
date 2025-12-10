# Day 10: Part 2
import re
import math
from heapq import heappush, heappop

# Variables
total = 0

try:
    with open("input.txt", "r") as file:
        # Convert each line into a machine info
        for line in file:
            buttons = []
            targets = ()

            button = re.findall(r'\(([\d,]+)\)', line)
            for b in button:
                buttons.append(tuple(map(int, b.split(','))))

            target = re.search(r'\{([\d,]+)\}', line)
            if target:
                targets = tuple(map(int, target.group(1).split(',')))

            # Use A* algortirm to find lowest number pressed
            cost = 0
            counterLength = len(targets)

            # Find the most increment any button do
            maxImpact = max(len(b) for b in buttons) if buttons else 1

            startState = tuple([0] * counterLength)
            priorityQueue = [(0, 0, startState)] # (estimatedTotalCost, currentCost, currentStateTuple)
            visited = set()
            visited.add(startState)

            while priorityQueue:
                _, cost, current = heappop(priorityQueue)

                if current == targets:
                    break

                # Skip if we have exceeded any target
                if any(c > t for c, t in zip(current, targets)):
                    continue

                # Try pressing each button
                for buttonIndices in buttons:
                    newCounts = list(current)
                    for idx in buttonIndices:
                        if idx < len(newCounts):
                            newCounts[idx] += 1
                        else:
                            break
                    newState = tuple(newCounts)

                    if newState in visited:
                        continue
                        
                    # Check for immediate overshoot to prune early
                    if any(n > t for n, t in zip(newState, targets)):
                        continue

                    visited.add(newState)
                    
                    # Find the minimum presses needed to cover remaining sum
                    remainingDifference = [t - n for t, n in zip(targets, newState)]
                    massNeeded = sum(remainingDifference)
                    heuristic = math.ceil(massNeeded / maxImpact)
                    
                    newCost = cost + 1
                    
                    heappush(priorityQueue, (newCost + heuristic, newCost, newState))
            
            total += cost

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)