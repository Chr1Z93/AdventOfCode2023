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

lastHit = None
lastId = None
lastEnd = None


def getValueFromFakeArray(id, key):
    global lastHit
    global lastId
    global lastEnd

    # try last matching interval first
    if id == lastId and lastEnd >= key and lastHit != None:
        if lastHit[0] <= key and lastHit[1] >= key:
            return lastHit[2] + key - lastHit[0]
    else:
        lastHit = None
        lastId = None
        lastEnd = None

    for d in listOfFakeArrays[id]:
        if d[0] <= key and d[1] >= key:
            lastHit = d
            lastId = id
            lastEnd = d[1]
            return d[2] + key - d[0]
    return key


def evaluateSeed(num):
    for i in range(0, 7):
        num = getValueFromFakeArray(i, num)
    return num


seedIntervals = []
listOfFakeArrays = []
for mapId, block in enumerate(splitInput):
    if mapId == 0:
        tempStr = block.split(":")
        seed = None
        for i, str in enumerate(tempStr[1].split()):
            if (i % 2) == 0:
                seed = int(str)
            else:
                seedIntervals.append([seed, int(str)])
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
i = 0
for seedList in seedIntervals:
    i += 1
    print(i)

    for j in range(seedList[1]):
        answer.append(evaluateSeed(seedList[0] + j))

print("Answer:", min(answer))
