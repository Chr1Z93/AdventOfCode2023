# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.
# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
# The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
# To play Camel Cards, you are given a list of hands and their corresponding bid.
# Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
# To balance this, J cards are now the weakest individual cards, weaker even than 2.
# Find the rank of every hand in your set. What are the total winnings?

from pathlib import Path
from functools import cmp_to_key

# get correct subfolder path
scriptPath = Path(__file__).resolve()
scriptDir = scriptPath.parent
inputPath = scriptDir / "input.txt"
f = open(inputPath)

cardList = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


# returns positive if the first card is better
def compareCards(c1, c2):
    return cardList.index(c2) - cardList.index(c1)


# compares the rank of two hands by handData
def compareHands(hd1, hd2):
    # use hand rating if not equal
    if hd1["rating"] != hd2["rating"]:
        return hd1["rating"] - hd2["rating"]

    # compare cards from front to back for equal rating
    for i in range(0, 6):
        c1 = hd1["hand"][i]
        c2 = hd2["hand"][i]
        if c1 != c2:
            return compareCards(c1, c2)

    # if fully equal
    return 0


# count card occurences in hand
def getCardCounts(hand):
    if hand == "JJJJJ":
        return [5]

    cardCounts = []
    jokerCount = 0
    for c in cardList:
        count = hand.count(c)
        if c == "J":
            jokerCount = count
        elif count != 0:
            cardCounts.append(count)
    cardCounts.sort(reverse=True)
    cardCounts[0] = cardCounts[0] + jokerCount
    return cardCounts


# get poker hand rating
def getRatingFromCounts(counts):
    if counts[0] == 5:
        return 6  # five of a kind
    elif counts[0] == 4:
        return 5  # four of a kind
    elif counts[0] == 3 and counts[1] == 2:
        return 4  # full house
    elif counts[0] == 3:
        return 3  # three of a kind
    elif counts[0] == 2 and counts[1] == 2:
        return 2  # two pair
    elif counts[0] == 2:
        return 1  # one pair
    else:
        return 0  # high card


# get metadata for each line and sort by rank
data = []
for lineIndex, line in enumerate(f):
    tempStr = line.split()
    counts = getCardCounts(tempStr[0])
    rating = getRatingFromCounts(counts)
    handData = {
        "bid": int(tempStr[1]),
        "hand": tempStr[0],
        "rating": rating,
    }
    data.append(handData)
data.sort(key=cmp_to_key(compareHands))

# calculate total winnings
answer = 0
for i, hd in enumerate(data):
    answer += (i + 1) * hd["bid"]
print(answer)
