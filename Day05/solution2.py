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
    for i, d in enumerate(listOfFakeArrays[id]):
        if d[0] > key:
            return key
        elif d[1] < key:
            continue
        else:
            listOfFakeArrays[id] = listOfFakeArrays[id][i:]
            return d[2] + key - d[0]
    return key


def evaluateSeed(num):
    for id in range(0, 7):
        num = getValueFromFakeArray(id, num)
    return num


def getFirstEntry(entry):
    return entry[0]


seedIntervals = []
listOfFakeArrays = []
for mapId, block in enumerate(splitInput):
    if mapId == 0:
        seed = None
        for i, str in enumerate(block.split(":")[1].split()):
            if (i % 2) == 0:
                seed = int(str)
            else:
                seedIntervals.append([seed, int(str)])
        seedIntervals.sort(key=getFirstEntry)
    else:
        fArray = []
        for i, line in enumerate(StringIO(block)):
            if i != 0:
                tempStr = line.split()
                keyStart = int(tempStr[1])
                keyEnd = keyStart + int(tempStr[2]) - 1
                valueStart = int(tempStr[0])
                fArray.append([keyStart, keyEnd, valueStart])
        fArray.sort(key=getFirstEntry)
        listOfFakeArrays.append(fArray)

answer = None
for i, seedList in enumerate(seedIntervals):
    print("Seed id:", i)
    for j in range(seedList[1]):
        result = evaluateSeed(seedList[0] + j)
        if answer == None or result < answer:
            answer = result
print("Answer:", answer)
