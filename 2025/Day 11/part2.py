# Day 11: Part 2

# Variables
graph = {}
totalPath = 0

# Count paths between any two specific points
def countPath(start: str, target: str) -> int:
    memo = {} 

    def getSegment(node):
        if node in memo:
            return memo[node]
        
        # We reached the target for this segment
        if node == target:
            return 1
        
        # Node not in graph
        if node not in graph:
            return 0
        
        # Recursively find paths
        total = 0
        for neighbor in graph[node]:
            total += getSegment(neighbor)
        
        memo[node] = total
        return total

    return getSegment(start)

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip().split(' ')
            source = line[0][:-1]
            destinations = line[1:]
            graph[source] = destinations

        # Calculate all possible path
        route1 = countPath('svr', 'dac') * countPath('dac', 'fft') * countPath('fft', 'out')
        route2 = countPath('svr', 'fft') * countPath('fft', 'dac') * countPath('dac', 'out')
        totalPath = route1 + route2

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(totalPath)