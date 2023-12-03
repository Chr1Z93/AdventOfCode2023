# The engine schematic (your puzzle input) consists of a visual representation of the engine.
# A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.
# This time, you need to find the gear ratio of every gear and add them all up.

from pathlib import Path
import re

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

numberTable = []
symbolTable = []

# parse input into tables
for lineIndex, line in enumerate(f):
    # get numbers
    numberTable.append([])
    for match in re.finditer("[0-9]+", line):
        find = {
            "value": int(match.group()),
            "start": int(match.start()),
            "end": int(match.end()),
        }
        numberTable[lineIndex].append(find)

    # get symbols
    symbolTable.append([])
    for match in re.finditer("\*", line):
        find = {"id": lineIndex, "symbol": match.group(), "pos": int(match.start())}
        symbolTable[lineIndex].append(find)


# get answer
answer = 0
for lineIndex, line in enumerate(symbolTable):
    for sHit in line:
        partNumbers = []
        # get part numbers above
        if lineIndex != 0:
            for nHit in numberTable[lineIndex - 1]:
                if sHit["pos"] >= (nHit["start"] - 1) and sHit["pos"] <= (nHit["end"]):
                    partNumbers.append(nHit["value"])

        # get part numbers in the same line
        for nHit in numberTable[lineIndex]:
            if sHit["pos"] >= (nHit["start"] - 1) and sHit["pos"] <= (nHit["end"]):
                partNumbers.append(nHit["value"])

        # get part numbers below
        if lineIndex != (len(numberTable) - 1):
            for nHit in numberTable[lineIndex + 1]:
                if sHit["pos"] >= (nHit["start"] - 1) and sHit["pos"] <= (nHit["end"]):
                    partNumbers.append(nHit["value"])

        # add to answer if two part numbers found
        if len(partNumbers) == 2:
            answer += partNumbers[0] * partNumbers[1]
print(answer)
