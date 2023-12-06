# Holding down the button charges the boat, and releasing the button allows the boat to move.
# Boats move faster if their button was held longer, but time spent holding the button counts against the total race time.
# You can only hold the button at the start of the race, and boats don't move until the button is released.
# There's really only one race - ignore the spaces between the numbers on each line.
# How many ways can you beat the record in this one much longer race?

from pathlib import Path
from numpy import prod

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)


# parse input into tables
data = []
for i, line in enumerate(f):
    tempStr = line.split(":")[1].replace(" ", "")
    data.append(int(tempStr))

# get ways to win
waysToWin = []
time = data[0]
distance = data[1]
halfPoint = round(time, 0)

# parse from the front (back is symmetrical)
result = 0
for speed in range(1, halfPoint):
    if speed * (time - speed) > distance:
        result += 1
waysToWin.append(result)

print(prod(waysToWin))
