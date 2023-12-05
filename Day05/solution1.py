# The almanac (your puzzle input) lists all of the seeds that need to be planted.
# It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil,
# what type of water to use with each kind of fertilizer, and so on.
# Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category
# - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.
# What is the lowest location number that corresponds to any of the initial seed numbers?

from pathlib import Path
import io
import time


def generateMap(tempStr):
    keyStart = int(tempStr[1])
    keyCount = int(tempStr[2])
    valueStart = int(tempStr[0])
    return dict.fromkeys(range(keyStart, keyStart + keyCount), [valueStart, keyStart])


def getValue(mapId, key):
    value = mapOfMaps[mapId].get(key, key)
    if value != key:
        value = value[0] + key - value[1]
    return value


# get the start time
start = time.time()

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
data = Path(inputPath).read_text()
splitInput = data.split("\n\n")

seeds = []
mapOfMaps = {}

for i in range(1, 8):
    mapOfMaps[i] = {}

for mapId, block in enumerate(splitInput):
    if mapId == 0:
        tempStr = block.split(":")
        seeds = tempStr[1].split()
    else:
        map = mapOfMaps[mapId]
        for i, line in enumerate(io.StringIO(block)):
            if i != 0:
                newMap = generateMap(line.split())
                map.update(newMap)
    print("mapId:", mapId, "Time:", time.time() - start)

answer = 0
for seed in seeds:
    num = int(seed)
    result1 = getValue(1, num)
    result2 = getValue(2, result1)
    result3 = getValue(3, result2)
    result4 = getValue(4, result3)
    result5 = getValue(5, result4)
    result6 = getValue(6, result5)
    result7 = getValue(7, result6)

    # print("Seed:", num)
    # print("Conversion:", result1, result2, result3, result4, result5, result6, result7)

    if answer == 0 or answer > result7:
        answer = result7
print("Answer:", answer)
print("Time: ", time.time() - start)
