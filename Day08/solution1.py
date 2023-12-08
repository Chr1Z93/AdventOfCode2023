# It seems like you're meant to use the left/right instructions to navigate the network.
# Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now,
# and you have to follow the left/right instructions until you reach ZZZ.
# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

from pathlib import Path
from re import findall

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = Path(inputPath).read_text()
splitInput = f.split("\n\n")


# parse instructions into list
instructions = []
for c in splitInput[0]:
    if c == "L":
        instructions.append(0)
    else:
        instructions.append(1)

# parse data into dictionary
map = {}
for line in splitInput[1].split("\n"):
    result = findall("(\w+)", line)
    key = result[0]
    value = [result[1], result[2]]
    map[key] = value

i = 0
location = "AAA"
while location != "ZZZ":
    id = i % len(instructions)
    listIndex = instructions[id]
    list = map[location]
    location = list[listIndex]
    i += 1

print(i)
