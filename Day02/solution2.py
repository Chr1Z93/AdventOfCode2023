# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# For each game, find the minimum set of cubes that must have been present.
# What is the sum of the power of these sets?

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
def getColorData(set):
    # get values for colors
    valueData = set.split(",")
    colorData = {"red": 0, "green": 0, "blue": 0}

    for singleColorData in valueData:
        color = re.findall("[a-z]+", singleColorData)[0]
        colorData[color] = int(re.findall("[0-9]+", singleColorData)[0])
    return colorData


answer = 0

for line in f:
    # get ID from game
    tempStr = line.split(":")
    gameId = int(tempStr[0][5:])

    data = tempStr[1]

    # get subsets in this
    setData = data.split(";")

    # track color data
    gameColorData = {"red": 0, "green": 0, "blue": 0}

    # get single data and update total data
    for str in setData:
        singleColorData = getColorData(str)
        gameColorData["red"] = max(gameColorData["red"], singleColorData["red"])
        gameColorData["green"] = max(gameColorData["green"], singleColorData["green"])
        gameColorData["blue"] = max(gameColorData["blue"], singleColorData["blue"])

    # get power of the game and add to answer
    answer += gameColorData["red"] * gameColorData["green"] * gameColorData["blue"]

print(answer)
