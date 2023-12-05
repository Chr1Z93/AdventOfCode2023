# The almanac (your puzzle input) lists all of the seeds that need to be planted.
# It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil,
# what type of water to use with each kind of fertilizer, and so on.
# Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category
# - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.
# The values on the initial seeds: line come in pairs.
# Within each pair, the first value is the start of the range and the second value is the length of the range.
# What is the lowest location number that corresponds to any of the initial seed numbers?

from pathlib import Path
from io import StringIO

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
data = Path(inputPath).read_text()
splitInput = data.split("\n\n")


def getValueFromFakeArray(id, key):
    for d in listOfFakeArrays[id]:
        if d[0] < key and d[1] >= key:
            return d[2] + key - d[0]
    return key


def evaluateSeed(num):
    for i in range(0, 7):
        num = getValueFromFakeArray(i, num)
    return num


seeds = []
listOfFakeArrays = []

for mapId, block in enumerate(splitInput):
    if mapId == 0:
        tempStr = block.split(":")
        seeds = tempStr[1].split()
    else:
        fArray = []
        for i, line in enumerate(StringIO(block)):
            if i != 0:
                tempStr = line.split()
                keyStart = int(tempStr[1])
                keyEnd = keyStart + int(tempStr[2]) - 1
                valueStart = int(tempStr[0])
                fArray.append([keyStart, keyEnd, valueStart])
        listOfFakeArrays.append(fArray)

answer = []
seed = None
for i, str in enumerate(seeds):
    if (i % 2) == 0:
        seed = int(str)
    else:
        for j in range(int(str)):
            answer.append(evaluateSeed(seed + j))

print("Answer:", min(answer))
