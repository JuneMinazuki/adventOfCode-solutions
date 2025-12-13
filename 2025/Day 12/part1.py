# Day 12: Part 1

# Variables
total = 0

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()

            # Check if line contain "x"
            if "x" in line:
                parts = line.split()

                # Remove the colon and split by x
                rawSize = parts[0][:-1]
                size = rawSize.split("x")
                area = int(size[0]) * int(size[1])

                # Calculate sum of presents
                presents = 0
                for n in range(1, len(parts)):
                    presents += int(parts[n])

                # Check if area meets the requirement
                if area >= (presents * 9):
                    total += 1

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)

