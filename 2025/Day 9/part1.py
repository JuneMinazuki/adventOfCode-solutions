# Day 9: Part 1

# Variables
coordinate = []
maxArea = 0

try:
    with open("input.txt", "r") as file:
        # Seperate each line into a coordinate
        for line in file:
            point = line.strip().split(",")
            coordinate.append((int(point[0]), int(point[1])))

        # Find the biggest area
        for i in range(len(coordinate)):
            for j in range(i + 1, len(coordinate)):
                area = (abs(coordinate[i][0] - coordinate[j][0]) + 1) * (abs(coordinate[i][1] - coordinate[j][1]) + 1)

                if (area > maxArea):
                    maxArea = area

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(maxArea)