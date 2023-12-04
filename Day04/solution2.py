# Specifically, you win copies of the scratchcards below the winning card equal to the number of matches.
# Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied.
# Process all of the original and copied scratchcards until no more scratchcards are won.
# Including the original set of scratchcards, how many total scratchcards do you end up with?

from pathlib import Path

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"

cardCount = {}

# initialize cardCount
for lineIndex, line in enumerate(open(inputPath), start=1):
    cardCount[lineIndex] = 1

# parse input into tables
for lineIndex, line in enumerate(open(inputPath), start=1):
    tempStr = line.split(":")
    tempStr = tempStr[1].split("|")

    # get picked numbers
    pickedNumbers = tempStr[0].split()

    # get winning numbers
    winningNumbers = tempStr[1].split()

    # count overlap
    overlap = set(pickedNumbers).intersection(winningNumbers)
    count = len(overlap)

    # increase amount of next tickets
    if count > 0:
        for i in range(1, count + 1):
            cardCount[lineIndex + i] += cardCount[lineIndex]

# calculate total amount
print(sum(cardCount.values()))
