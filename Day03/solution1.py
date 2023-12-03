# The engine schematic (your puzzle input) consists of a visual representation of the engine.
# There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol,
# even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
# What is the sum of all of the part numbers in the engine schematic?

from pathlib import Path
import re

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)


def checkIfSymbolIsNear(nHit, symbolIndex):
    for sHit in symbolTable[symbolIndex]:
        if sHit["pos"] >= (nHit["start"] - 1) and sHit["pos"] <= (nHit["end"]):
            return True
    return False


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
    for match in re.finditer("[^.\d\n]", line):
        find = {"id": lineIndex, "symbol": match.group(), "pos": int(match.start())}
        symbolTable[lineIndex].append(find)

# get answer
answer = 0
for lineIndex, line in enumerate(numberTable):
    for hit in line:
        # check if there is a symbol in the same line
        hit["part"] = checkIfSymbolIsNear(hit, lineIndex)

        # check if there is a symbol in the next line
        if lineIndex != (len(numberTable) - 1) and hit["part"] != True:
            hit["part"] = checkIfSymbolIsNear(hit, lineIndex + 1)

        # check if there is a symbol in the previous line
        if lineIndex != 0 and hit["part"] != True:
            hit["part"] = checkIfSymbolIsNear(hit, lineIndex - 1)

        # sum part numbers
        if hit["part"] == True:
            answer += hit["value"]
print(answer)
