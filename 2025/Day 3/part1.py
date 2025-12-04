# Day 3: Part 1

try:
    # Variables
    total = 0

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()

            firstDigitOption = line[:-1]

            # Find the largest number in firstDigitOption
            firstDigit = max(firstDigitOption)
            for i in range(len(firstDigitOption)):
                if (firstDigit == firstDigitOption[i]):
                    break

            # Get secondDigitOption
            secondDigitOption = line[i+1:]
            secondDigit = max(secondDigitOption)

            total += int(f"{firstDigit}{secondDigit}")
                
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)