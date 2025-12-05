# Day 5: Part 2

try:
    # Variables
    ranges = []
    mergedRanges = []
    total = 0

    with open("input.txt", "r") as file:
        content = file.read()
        sections = content.strip().split("\n\n") 

        # Get ranges
        inputRanges = sections[0].splitlines()
        for line in inputRanges: 
            num = line.strip().split("-")
            numStart = int(num[0])
            numEnd = int(num[1])

            ranges.append((numStart, numEnd))

        # Merge overlapping ranges together
        sortedRanges = sorted(ranges, key=lambda x: x[0])
        for currentStart, currentEnd in sortedRanges:
            if not mergedRanges:
                mergedRanges.append([currentStart, currentEnd])
            else:
                # Get the previous range added
                previousStart, previousEnd = mergedRanges[-1]

                if currentStart <= previousEnd: # Found overlapped
                    mergedRanges[-1][1] = max(previousEnd, currentEnd)
                else: # No overlapped
                    mergedRanges.append([currentStart, currentEnd])

        # Count total of all ranges
        for start, end in mergedRanges:
            total += end - start + 1

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(total)