# Day 4: Part 1

try:
    # Variables
    coordinate = set()
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    acceptedTile = 0

    with open("input.txt", "r") as file:
        # Get coordinate of each @
        for x, line in enumerate(file):
            line = line.strip()

            for y, tile in enumerate(line):
                if (tile == '@'):
                    coordinate.add((x,y))

        # Loop through every tile and check
        for x, y in coordinate:
            count = 0

            for dx, dy in neighbors:
                nx = x + dx
                ny = y + dy

                # Check if coodinate contains [nx, ny]
                if ((nx, ny) in coordinate):
                    count += 1
            
            if (count < 4):
                acceptedTile += 1

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(acceptedTile)