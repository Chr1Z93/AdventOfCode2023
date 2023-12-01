# On each line, the calibration value can be found by combining the first digit (can be spelled out!)
# and the last digit (can be spelled out!, in that order) to form a single two-digit number.
# What is the sum of all of the calibration values?

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input1.txt"

debug = False

f = open(inputPath)

numberWords = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def getDigitWordFromString(str, mode):
    digitWord = ""
    posWord = -1

    if mode == "first":
        for word in numberWords.keys():
            tempPos = str.find(word)
            if tempPos != -1 and (posWord == -1 or tempPos < posWord):
                posWord = tempPos
                digitWord = word
    else:
        for word in numberWords.keys():
            tempPos = str[::-1].find(word[::-1])
            if tempPos != -1 and (posWord == -1 or tempPos < posWord):
                posWord = tempPos
                digitWord = word

    if posWord != -1:
        if mode == "last":
            posWord = len(str) - 1 - posWord
        return numberWords[digitWord], posWord
    else:
        return "", -1


def getDigitCharFromString(str, mode):
    if mode == "first":
        pos = -1
        for char in str:
            pos += 1
            if char.isdigit():
                return char, pos
    else:
        pos = len(str)
        for char in reversed(str):
            pos -= 1
            if char.isdigit():
                return char, pos
    return "", -1


answer = 0

for line in f:
    firstChar = ""
    secondChar = ""

    # get first actual digit
    char1, char1Pos = getDigitCharFromString(line, "first")

    # get first spelled out digit
    word1, word1Pos = getDigitWordFromString(line, "first")

    # get last digit
    char2, char2Pos = getDigitCharFromString(line, "last")

    # get last spelled out digit
    word2, word2Pos = getDigitWordFromString(line, "last")

    # get first digit
    if char1Pos == -1:
        firstChar = word1
    elif word1Pos == -1:
        firstChar = char1
    elif word1Pos < char1Pos:
        firstChar = word1
    else:
        firstChar = char1

    # get last digit
    if char2Pos == -1:
        secondChar = word2
    elif word2Pos == -1:
        secondChar = char2
    elif word2Pos > char2Pos:
        secondChar = word2
    else:
        secondChar = char2

    if debug:
        print(line)
        print("Char1: " + char1 + " / " + str(char1Pos))
        print("Word1: " + word1 + " / " + str(word1Pos))
        print("Char2: " + char2 + " / " + str(char2Pos))
        print("Word2: " + word2 + " / " + str(word2Pos))
        print(int(firstChar + secondChar))

    # combine both digits and add to answer
    answer += int(firstChar + secondChar)

print(answer)
