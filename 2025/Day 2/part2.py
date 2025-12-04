# Day 2: Part 2
import math

try:
    # Variables
    total = 0
    ids = list()

    with open("input.txt", "r") as file:
        ids = file.readline().strip().split(",")

        for id in ids:
            # Get range of number
            num = id.split("-")
            numStart = int(num[0])
            numEnd = int(num[1])
            numChecked = set()

            # Find the length of number to test until
            lengthToTestUntil = math.ceil(len(num[1]) / 2)
            numToTestUntil = int("9" * lengthToTestUntil)
            currentNum = 1

            while (currentNum <= numToTestUntil):
                # Convert currentNum to string and loop for every repeat
                s_currentNum = str(currentNum)
                numToRepeat = currentNum

                # Check if currentNum have been tested before
                if (numToRepeat not in numChecked):
                    while (numToRepeat <= numEnd):
                        numToRepeat = int(str(numToRepeat) + s_currentNum)

                        # Check if numToRepeat is in the range
                        if (numToRepeat >= numStart and numToRepeat <= numEnd):
                            total += numToRepeat
                            numChecked.add(numToRepeat)
                
                currentNum += 1
            
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)