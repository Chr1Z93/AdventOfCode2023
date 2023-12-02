# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.
# What is the sum of all of the calibration values?

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"

f = open(inputPath)

answer = 0
firstChar = ""
secondChar = ""

for line in f:
    # get first digit
    for char in line:
        if char.isdigit():
            firstChar = char
            break

    # get last digit
    for char in reversed(line):
        if char.isdigit():
            secondChar = char
            break

    # combine both digits and add to answer
    answer += int(firstChar + secondChar)

print(answer)
