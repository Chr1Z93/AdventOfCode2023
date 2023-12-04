# Specifically, you win copies of the scratchcards below the winning card equal to the number of matches.
# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied.
# Process all of the original and copied scratchcards until no more scratchcards are won.
# Including the original set of scratchcards, how many total scratchcards do you end up with?

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

answer = 0
cardCount = {}

# initialize cardCount
for lineIndex, line in enumerate(f):
    cardCount[lineIndex] = 1

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
