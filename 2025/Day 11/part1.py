# Day 11: Part 1

# Variables
graph = {}
memo = {}
totalPath = 0

def getPath(node: str) -> int:
    # Check if we already calculated this node
    if node in memo:
        return memo[node]
    
    # We reached the end
    if node == 'out':
        return 1
    
    # Node isn't in our list of sources
    if node not in graph:
        return 0
    
    # Find sum of paths from all neighbors
    total = 0
    for neighbor in graph[node]:
        total += getPath(neighbor)
    
    # Save the result before returning
    memo[node] = total
    return total

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip().split(' ')
            source = line[0][:-1]
            destinations = line[1:]
            graph[source] = destinations

        # Find sum of paths from all node
        totalPath = getPath('you')

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(totalPath)