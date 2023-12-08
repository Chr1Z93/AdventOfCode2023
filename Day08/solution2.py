# It seems like you're meant to use the left/right instructions to navigate the network.
# Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!
# Start at every node that ends with A and follow all of the paths at the same time
# until they all simultaneously end up at nodes that end with Z..
# How many steps does it take before you're only on nodes that end with Z?

from pathlib import Path
from re import findall

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "example.txt"
f = Path(inputPath).read_text()
splitInput = f.split("\n\n")


# parse instructions into list
instructions = []
for c in splitInput[0]:
    if c == "L":
        instructions.append(0)
    else:
        instructions.append(1)
length = len(instructions)

# parse data into dictionary
map = {}
locations = []
for line in splitInput[1].split("\n"):
    result = findall("(\w+)", line)
    key = result[0]
    value = [result[1], result[2]]
    map[key] = value

    if key[2] == "A":
        locations.append(key)

i = 0
keepGoing = True
while keepGoing:
    keepGoing = False
    id = instructions[i % length]
    newLocations = []
    for loc in locations:
        newLoc = map[loc][id]
        newLocations.append(newLoc)
        if not keepGoing and newLoc[2] != "Z":
            keepGoing = True
    locations = newLocations
    i += 1
    print("Id:", i, "Locations:", locations)
