# Day 4: Part 2

try:
    # Variables
    coordinate = set()
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    acceptedTile = 0
    initialAcceptedTile = -1

    with open("input.txt", "r") as file:
        # Get coordinate of each @
        for x, line in enumerate(file):
            line = line.strip()

            for y, tile in enumerate(line):
                if (tile == '@'):
                    coordinate.add((x,y))

        # Loop through every tile and check
        while (initialAcceptedTile != acceptedTile):
            initialAcceptedTile = acceptedTile

            for x, y in set(coordinate):
                count = 0

                for dx, dy in neighbors:
                    nx = x + dx
                    ny = y + dy

                    # Check if coodinate is out of bound and is @
                    if ((nx, ny) in coordinate):
                        count += 1
                
                if (count < 4):
                    acceptedTile += 1
                    coordinate.remove((x,y))

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(acceptedTile)