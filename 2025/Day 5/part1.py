# Day 5: Part 1
import bisect

# Variables
ranges = []
mergedRanges = []
count = 0

try:
    with open("test.txt", "r") as file:
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

        # Get all start of ranges
        rangeStart = [r[0] for r in mergedRanges]

        # Binary search
        searches = sections[1].splitlines()
        for n in searches: 
            # Find the smallest rangeStart that n fit into
            index = bisect.bisect_right(rangeStart, int(n))
            if (index == 0):
                continue

            # Check if number is in range
            end = mergedRanges[index - 1][1]
            if (int(n) <= end):
                count += 1
                print(f"{n} at range: [{mergedRanges[index - 1][0]}, {mergedRanges[index - 1][1]}]")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Output answer
print(count)