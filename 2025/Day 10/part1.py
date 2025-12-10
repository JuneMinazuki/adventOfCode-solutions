# Day 10: Part 1
import re

# Variables
lightOutput = []
machinesButton = []
total = 0

try:
    with open("input.txt", "r") as file:
        # Convert each line into a machine info
        for line in file:
            output = re.search(r'\[([.#]+)\]', line)
            if (not output):
                continue
            lightOutput.append(output.group(1).replace('.', '0').replace('#', '1'))

            machinesButton.append(re.findall(r'\(([\d,]+)\)', line))

        # Use Gaussian Solver to find the minimum button pressed
        for i in range(len(lightOutput)):
            lightLength = len(lightOutput[i])
            buttonLength = len(machinesButton[i])

            # Build a matrix where row is lights, and column is buttons
            matrix = []
            for l in range(lightLength):
                # Coefficient of 1 if button is connected to the light, else 0
                row = []
                currentButtons = machinesButton[i]

                for button in currentButtons:
                    indices = [int(x) for x in button.split(',')]
                    val = 1 if l in indices else 0
                    row.append(val)

                # Add light value
                row.append(int(lightOutput[i][l]))
                matrix.append(row)

            pivotRow = 0
            pivotCol = []

            # Forward elimination
            for col in range(buttonLength):
                if pivotRow >= lightLength:
                    break
                
                # Find a row with a 1 in this column to pivot
                candidate = -1
                for row in range(pivotRow, lightLength):
                    if matrix[row][col] == 1:
                        candidate = row
                        break
                
                if candidate == -1:
                    continue # This is a free variable column
                
                # Swap current row with candidate row
                matrix[pivotRow], matrix[candidate] = matrix[candidate], matrix[pivotRow]
                
                # Eliminate other rows
                for row in range(lightLength):
                    if row != pivotRow and matrix[row][col] == 1:
                        # Do XOR for current row and pivot row
                        for c in range(col, buttonLength + 1):
                            matrix[row][c] ^= matrix[pivotRow][c]
                
                pivotCol.append(col)
                pivotRow += 1

            # Identify free variables (0,0,0,0) and find fewest presses
            freeColumns = [c for c in range(buttonLength) if c not in pivotCol]
            freeNumber = len(freeColumns)
            minPresses = float('inf')

            # Try all combinations if there is free variables
            for bits in range(1 << freeNumber):
                solution = [0] * buttonLength
                currentWeight = 0

                # Assign free variables
                for idx, freeCol in enumerate(freeColumns):
                    val = (bits >> idx) & 1
                    solution[freeCol] = val
                    if val: currentWeight += 1
                
                # Back-substitute to find pivot variables
                for row in range(len(pivotCol) - 1, -1, -1):
                    pCol = pivotCol[row]
                    rowVal = matrix[row][buttonLength]
                    
                    # Subtract (XOR) the effect of the free variables
                    for freeCol in freeColumns:
                         if freeCol > pCol:
                            if matrix[row][freeCol] == 1 and solution[freeCol] == 1:
                                rowVal ^= 1
                    
                    solution[pCol] = rowVal
                    if rowVal: currentWeight += 1

                if currentWeight < minPresses:
                    minPresses = currentWeight

            total += minPresses

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)