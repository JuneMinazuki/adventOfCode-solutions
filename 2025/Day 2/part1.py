# Day 2: Part 1
import math

# Variables
total = 0
ids = list()

try:
    with open("input.txt", "r") as file:
        ids = file.readline().strip().split(",")

        for id in ids:
            # Get range of number
            num = id.split("-")
            numStart = num[0]
            numEnd = int(num[1])

            # Find where is the half of numStart
            spiltBy = math.ceil(len(numStart) / 2)

            # Get the first duplicate number to check
            if (len(numStart) % 2 == 0):
                checkDuplicate = int(numStart[:spiltBy])
            else:
                checkDuplicate = int(pow(10, spiltBy - 1))
            currentNum = int(f"{checkDuplicate}{checkDuplicate}")
            
            while (currentNum <= numEnd):
                if (currentNum >= int(numStart)):
                    total += currentNum

                checkDuplicate += 1
                currentNum = int(f"{checkDuplicate}{checkDuplicate}")
                
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)