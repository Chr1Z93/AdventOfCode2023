# As far as the Elf has been able to figure out, you have to figure out
# which of the numbers you have appear in the list of winning numbers.
# The first match makes the card worth one point
# and each match after the first doubles the point value of that card.

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

answer = 0

# parse input into tables
for lineIndex, line in enumerate(f):
    tempStr = line.split(":")
    tempStr = tempStr[1].split("|")

    # get picked numbers
    pickedNumbers = tempStr[0].split()

    # get winning numbers
    winningNumbers = tempStr[1].split()

    # count overlap
    overlap = set(pickedNumbers).intersection(winningNumbers)
    count = len(overlap)

    # get value of the card (2^(n-1))
    value = 0
    if count > 0:
        value = 2 ** (count - 1)

    # add value to answer
    answer += value
print(answer)
