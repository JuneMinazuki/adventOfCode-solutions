# Day 7: Part 2
from collections import defaultdict

try:
    # Variables
    spilter = set()
    startingColumn = int()
    totalRow = 0

    with open("input.txt", "r") as file:
        # Get coordinate of each ^ and 'S'
        for row, line in enumerate(file):
            line = line.strip()

            for column, tile in enumerate(line):
                if (tile == '^'):
                    spilter.add((row, column))
                elif (tile == 'S'):
                    startingColumn = column
            totalRow += 1

        # Check if number of beam in each column
        currentBeam = defaultdict(int)
        currentBeam[startingColumn] = 1

        for row in range(totalRow):
            nextBeam = defaultdict(int)
            for column, count in currentBeam.items():
                if ((row, column) in spilter):
                    nextBeam[column - 1] += count
                    nextBeam[column + 1] += count
                else:
                    nextBeam[column] += count
                
            currentBeam = nextBeam
        
        count = sum(currentBeam.values())

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(count)