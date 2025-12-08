# Day 3: Part 2

# Variables
total = 0

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()

            lineLength = len(line)
            indexLength = lineLength - 11
            currentValue = str()
            i = 0

            for x in range(12):
                digitOption = line[i:i + indexLength]
                
                # Find the largest number in digitOption
                digit = max(digitOption)
                currentValue = f"{currentValue}{digit}"
                i += digitOption.index(digit) + 1
                indexLength -= digitOption.index(digit)
                
            total += int(currentValue)
                
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)