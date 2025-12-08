# Day 6: Part 1

# Variables
number = []
total = 0

try:
    with open("input.txt", "r") as file:
        content = file.read()
        lines = content.strip().split("\n") 

        operation = lines[-1].split()

        # Convert each row into list of number
        for n in range(len(lines) - 1):
            number.append(lines[n].split())

        # Process each operation column by column
        for col, operant in enumerate(operation):
            currentValue = 0 if (operant == '+') else 1

            if (operant == '+'):
                for i in range(len(number)):
                    currentValue += int(number[i][col])
            else:
                for i in range(len(number)):
                    currentValue *= int(number[i][col])

            # Add up all answer
            total += currentValue

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)