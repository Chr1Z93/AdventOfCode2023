# Determine which games would have been possible if the bag had been loaded
# with only 12 red cubes, 13 green cubes, and 14 blue cubes.
# What is the sum of the IDs of those games?

from pathlib import Path
import re

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"

f = open(inputPath)

# set bag configuration
maxRed = 12
maxGreen = 13
maxBlue = 14


# check if a set is legal
def isSetLegal(set):
    # get values for colors
    valueData = set.split(",")

    colorData = {"red": 0, "green": 0, "blue": 0}

    for singleColorData in valueData:
        color = re.findall("[a-z]+", singleColorData)[0]
        colorData[color] = int(re.findall("[0-9]+", singleColorData)[0])

    if (
        colorData["red"] <= maxRed
        and colorData["blue"] <= maxBlue
        and colorData["green"] <= maxGreen
    ):
        return True
    else:
        return False


answer = 0

for line in f:
    # get ID from game
    tempStr = line.split(":")
    gameId = int(tempStr[0][5:])

    data = tempStr[1]

    # get subsets in this
    setData = data.split(";")

    # check if game is legal

    legal = True
    for str in setData:
        if not isSetLegal(str):
            legal = False
            break

        # add to answer
    if legal:
        answer += gameId

print(answer)
