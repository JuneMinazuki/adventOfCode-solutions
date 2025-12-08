# Day 1: Part 2

# Variables
currentDial = 50
count = 0

try:
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            
            direction = line[0]
            speed = int(line[1:])
            
            if (direction == "L"):
                # Find steps needed to hit 0 from current position
                if (currentDial > 0):
                    distToZero = currentDial 
                else:
                    distToZero = 100 
                
                # 1 (for the first hit) + (remaining speed // 100) for subsequent loops
                if speed >= distToZero:
                    count += 1 + (speed - distToZero) // 100
                
                # Update dial position
                currentDial = (currentDial - speed) % 100

            elif (direction == "R"):
                # Find steps needed to hit 0 from current position
                distToZero = 100 - currentDial

                # 1 (for the first hit) + (remaining speed // 100) for subsequent loops
                if speed >= distToZero:
                    count += 1 + (speed - distToZero) // 100
                
                # Update dial position
                currentDial = (currentDial + speed) % 100
            
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(count)