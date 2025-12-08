# Day 8: Part 1
import heapq
import collections

# Variables
points = []
answer = 0

# Find the two point with the stortest distance
def findShortestPoints(points: list[tuple]) -> list[tuple[tuple, tuple]]:
    def calculateDistance():
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pointA = points[i]
                pointB = points[j]
                
                # Calculate the distance between two points
                dist = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2 + (pointA[2] - pointB[2])**2
                
                # Store the distance and the two points in a heap
                yield (dist, (pointA, pointB))

    # Find the top 1000 pair and remove the distance
    bestPair = heapq.nsmallest(1000, calculateDistance())
    return [pair for dist, pair in bestPair]

try:
    with open("input.txt", "r") as file:
        # Get all coordinate
        for line in file:
            line = line.strip().split(",")
            points.append((int(line[0]), int(line[1]), int(line[2])))

        pairs = findShortestPoints(points)

        # Graph out a dict with coordinate as key, that is mapped to a list of connected corrdinates
        connection = collections.defaultdict(list)
        for coordinateA, coordinateB in pairs:
            connection[coordinateA].append(coordinateB)
            connection[coordinateB].append(coordinateA)

        # Loop through every unique point found in pairs
        visitedPoint = set()
        groupSize = []
        allPoints = list(connection.keys())

        for point in allPoints:
            # Start a new curcuit if point not visited before
            if (point not in visitedPoint):
                count = 0
                queue = collections.deque([point])
                visitedPoint.add(point)

                while queue:
                    currentPoint = queue.popleft()
                    count += 1
            
                    # Find all neighbors of the current curcuit
                    for neighbor in connection[currentPoint]:
                        if neighbor not in visitedPoint:
                            visitedPoint.add(neighbor)
                            queue.append(neighbor)
                
                # Store the group size
                groupSize.append(count)

        # Multiply the 3 largest groupSize
        groupSize.sort()
        answer = groupSize[-1] * groupSize[-2] * groupSize[-3]

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(answer)