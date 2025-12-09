# Day 9: Part 2

# Variables
coordinate = []
perimeter = set()
areas = []
maxArea = 0

# Get set of all point in the line
def lines(pointA: tuple, pointB: tuple) -> set:
    l = set()
    xMin, xMax = min(pointA[0], pointB[0]), max(pointA[0], pointB[0])
    yMin, yMax = min(pointA[1], pointB[1]), max(pointA[1], pointB[1])

    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            l.add((x, y))

    return l

# Check if the point cross the perimeter
def checkWithinPerimeter(pointA: tuple, pointB: tuple, perimeter: set) -> bool:
    xMin, xMax = min(pointA[0], pointB[0]), max(pointA[0], pointB[0])
    yMin, yMax = min(pointA[1], pointB[1]), max(pointA[1], pointB[1])

    for x, y in perimeter:
        if (xMin < x < xMax) and (yMin < y < yMax):
            return False
        
    return True

try:
    with open("input.txt", "r") as file:
        # Seperate each line into a coordinate
        for line in file:
            point = line.strip().split(",")
            coordinate.append((int(point[0]), int(point[1])))

        # Get the perimeter of the geometry shape
        for i in range(1, len(coordinate)):
            l = lines(coordinate[i - 1], coordinate[i])
            perimeter |= l
        perimeter |= lines(coordinate[-1], coordinate[0])

        # Calculate all possible area and sort them
        for i in range(len(coordinate)):
            for j in range(i + 1, len(coordinate)):
                area = (abs(coordinate[i][0] - coordinate[j][0]) + 1) * (abs(coordinate[i][1] - coordinate[j][1]) + 1)
                areas.append(((coordinate[i], coordinate[j]), area))
        areas.sort(key=lambda x: x[1], reverse=True)
        
        # Check if the area is within the perimeter
        for rectArea in areas:
            point, area = rectArea
            if checkWithinPerimeter(point[0], point[1], perimeter):
                maxArea = area
                break

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(maxArea)