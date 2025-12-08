# Day 6: Part 2

# Variables
colList = []
operation = []
number = [[]]
total = 0

try:
    with open("input.txt", "r") as file:
        content = file.read()
        lines = content.strip().split("\n")

        operation = lines[-1].split()

        # Convert each row into list of char
        for n in range(len(lines) - 1):
            colList.append(list(lines[n]))

        # Make sure all row have the same amount of column
        maxColLength = len(max(colList, key=len))
        
        for col in colList:
            if (len(col) < maxColLength): 
                col.extend([' '] * (maxColLength - len(col)))

        # Convert each column in a new number
        for n in range(maxColLength):
            newNumber = str()
            for x in range(len(colList)):
                newNumber += colList[x][n]

            if (newNumber == (" " * len(colList))):
                number.append([])
            else:
                number[-1].append(int(newNumber))

        # Process each operation list by list
        for col, operant in enumerate(operation):
            currentValue = 0 if (operant == '+') else 1

            if (operant == '+'):
                for i in range(len(number[col])):
                    currentValue += int(number[col][i])
            else:
                for i in range(len(number[col])):
                    currentValue *= int(number[col][i])

            # Add up all answer
            total += currentValue

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)