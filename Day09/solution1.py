# The OASIS produces a report of many values and how they are changing over time (your puzzle input).
# Each line in the report contains the history of a single value.
# To best protect the oasis, your environmental report should include a prediction of the next value in each history.
# To do this, start by making a new sequence from the difference at each step of your history.

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)


def getPrediction(str):
    # get values from line string
    values = []
    values.append(str.split())
    for i in range(0, len(values[0])):
        values[0][i] = int(values[0][i])

    # parse differences
    vList = values[0]
    while not checkIfAllEqual(vList):
        vList = getDifferences(values[-1])
        values.append(vList)

    # calculate prediction
    pNum = 0
    for entry in values:
        pNum += entry[-1]
    print(pNum)
    return pNum


def checkIfAllEqual(vList):
    for i in range(1, len(vList)):
        if vList[i] != vList[0]:
            return False
    return True


def getDifferences(vList):
    newList = []
    for i in range(1, len(vList)):
        newList.append(vList[i] - vList[i - 1])
    return newList


answer = 0
# parse input into tables
for lineIndex, line in enumerate(f):
    answer += getPrediction(line)
print(answer)
