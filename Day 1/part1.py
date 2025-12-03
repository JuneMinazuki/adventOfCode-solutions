# Day 1: Part 1

try:
    # Variables
    currentDial = 50
    count = 0

    with open("Day 1/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            
            direction = line[0]
            speed = int(line[1:])

            if (direction == "L"):
                currentDial -= speed
                while (currentDial < 0):
                    currentDial += 100

            elif (direction == "R"):
                currentDial += speed
                while (currentDial > 99):
                    currentDial -= 100
            
            # Check if currentDial is 0 
            if (currentDial == 0):
                count += 1

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(count)