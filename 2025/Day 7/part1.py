# Day 7: Part 1

# Variables
spilter = set()
startingColumn = int()
totalRow = 0
count = 0

try:
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

        # Check if beam hitted the spilter row by row
        currentBeam = {startingColumn}
        for row in range(totalRow):
            nextBeam = set()
            for beam in currentBeam:
                if ((row, beam) in spilter):
                    nextBeam.add(beam + 1)
                    nextBeam.add(beam - 1)
                    count += 1
                else:
                    nextBeam.add(beam)
                
            currentBeam = nextBeam

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(count)