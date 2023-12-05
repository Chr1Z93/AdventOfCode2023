# The almanac (your puzzle input) lists all of the seeds that need to be planted.
# It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil,
# what type of water to use with each kind of fertilizer, and so on.
# Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category
# - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.
# What is the lowest location number that corresponds to any of the initial seed numbers?

from pathlib import Path
import io
import gc

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
data = Path(inputPath).read_text()

seeds = []
mapOfMaps = {
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


def fillMap(map, keyStart, keyCount, valueStart):
    for i in range(keyStart, keyStart + keyCount):
        map[i] = valueStart + i - keyStart


splitInput = data.split("\n\n")
for mapId, block in enumerate(splitInput):
    print("mapId:", mapId)
    if mapId == 0:
        tempStr = block.split(":")
        seeds = tempStr[1].split()
    else:
        for i, line in enumerate(io.StringIO(block)):
            if i != 0:
                tempStr = line.split()
                map = mapOfMaps[mapId]
                fillMap(map, int(tempStr[1]), int(tempStr[2]), int(tempStr[0]))
                gc.collect()

answer = 0
for seed in seeds:
    num = int(seed)
    result1 = mapOfMaps[1].get(num, num)
    result2 = mapOfMaps[2].get(result1, result1)
    result3 = mapOfMaps[3].get(result2, result2)
    result4 = mapOfMaps[4].get(result3, result3)
    result5 = mapOfMaps[5].get(result4, result4)
    result6 = mapOfMaps[6].get(result5, result5)
    result7 = mapOfMaps[7].get(result6, result6)

    print("Seed:", num)
    print("Conversion:", result1, result2, result3, result4, result5, result6, result7)

    if answer == 0 or answer > result7:
        answer = result7
print("Answer:", answer)
