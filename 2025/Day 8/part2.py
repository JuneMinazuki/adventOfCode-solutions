# Day 8: Part 1

# Variables
points = []
connection = []
answer = 0

class DisjointSetUnion:
    def __init__(self, points):
        # Every point is its own group at start
        self.parent = {point: point for point in points}
        self.groupNumber = len(points)

    def find(self, point):
        # Find the root of the point
        if self.parent[point] != point:
            self.parent[point] = self.find(self.parent[point])
        return self.parent[point]

    def union(self, pointA, pointB):
        # Find the roots of both points
        rootA = self.find(pointA)
        rootB = self.find(pointB)

        # If they are in different groups, merge them
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.groupNumber -= 1
            return True 
        
        # Return false is they are already connected
        return False

try:
    with open("input.txt", "r") as file:
        # Get all coordinate
        for line in file:
            line = line.strip().split(",")
            points.append((int(line[0]), int(line[1]), int(line[2])))

        # Get a list of all connection and its distance
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pointA = points[i]
                pointB = points[j]
                
                # Calculate the distance between two points
                dist = (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2 + (pointA[2] - pointB[2])**2
                
                connection.append((dist, pointA, pointB))

        # Sort the connection by its distance
        connection.sort(key=lambda x: x[0])

        # Connect all point together
        dsu = DisjointSetUnion(points)
        connectionsMade = 0
        lastCoordinates = ((0, 0, 0), (0, 0, 0))
        
        for dist, pointA, pointB in connection:
            # Try to connect the two point
            if dsu.union(pointA, pointB):
                connectionsMade += 1
                lastCoordinates = (pointA, pointB)
                
                # Stop when there is only 1 group left
                if dsu.groupNumber == 1:
                    break
        
        # Multiply the x value of both point
        answer = lastCoordinates[0][0] * lastCoordinates[1][0]

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(answer)