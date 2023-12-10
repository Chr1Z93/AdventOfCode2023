# The pipes are arranged in a two-dimensional grid of tiles.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# Find the single giant loop starting at S. Figure out whether you have time to search for the nest by calculating the area within the loop.
# How many tiles are enclosed by the loop?

from pathlib import Path
from math import floor

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

# define pipe connections
pipeConnections = {
    "|": ["north", "south"],
    "-": ["west", "east"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["west", "south"],
    "F": ["east", "south"],
}

# define opposite direction
connected = {"north": "south", "south": "north", "west": "east", "east": "west"}


def getPathLength(pos, startDirection):
    L = 0
    while True:
        char = map[pos[0]][pos[1]]

        # if on "S" and not starting here or on ".", end loop
        if (char == ".") or (char == "S" and L != 0):
            break

        if char == "S":
            direction = startDirection
        else:
            direction = getDirection(char, direction)

        if direction == None:
            break

        pos = getNextPos(pos, direction)

        if pos == None:
            break

        L += 1
    return floor(L / 2)


def getDirection(char, oldDirection):
    newDirection = None
    isConnected = False
    for item in pipeConnections[char]:
        if connected[item] == oldDirection:
            isConnected = True
        else:
            newDirection = item
    if isConnected == False:
        return None
    else:
        return newDirection


def getNextPos(pos, direction):
    newPos = []
    if direction == "north":
        newPos = [pos[0] - 1, pos[1]]
    elif direction == "south":
        newPos = [pos[0] + 1, pos[1]]
    elif direction == "west":
        newPos = [pos[0], pos[1] - 1]
    elif direction == "east":
        newPos = [pos[0], pos[1] + 1]

    # validate new position
    if newPos[0] == -1 or newPos[0] == maxRow or newPos[1] == -1 or newPos[1] == maxCol:
        newPos = None
    return newPos


# get starting position (0-indexed: row, column) and parse into list
map = []
startPos = None
for lineIndex, line in enumerate(f):
    line = line.replace("\n", "")
    map.append(line)
    searchResult = line.find("S")

    if searchResult != -1:
        startPos = [lineIndex, searchResult]
maxRow = len(map)
maxCol = len(map[0])

# check surroundings for paths
answer = 0
for d in connected:
    t = getPathLength(startPos, d)
    if t != 0:
        answer = t
        break
print(answer)
