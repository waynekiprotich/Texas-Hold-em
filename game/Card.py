"""
Forces valid card values only.
Converts input to uppercase.
Prevents invalid cards, e.g., 'joker'
Stores rank + suit in an object
Print card details
"""

class Card():

    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITES = ["HEART", "DIAMOND", "SPADE", "CLUBS"]

    def __init__(self, suite, rank):

        if not isinstance(suite, str):
            raise TypeError(f"Suite expected to be a string got {type(suite).__name__}")
        
        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string got {type(rank).__name__}")

        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        if rankUpper in Card.RANKS:
            pass
        else:
            raise TypeError(f"Added rank not in rank list {Card.RANKS}")

        if suiteUpper in Card.SUITES:
            pass
        else:
            raise TypeError(f"Added suite not in suite list {Card.SUITES}")

        self.rank = rankUpper
        self.suite = suiteUpper

    def printCard(self):
        print("Rank:", self.rank)
        print("Suite:", self.suite)
        print("--------------------" )

if __name__ == "__main__":
    
    # Testing a valid card
    print("Testing Valid Card:")
    card2 = Card(suite="SPADE", rank="5")
    card2.printCard()

    # Testing an invalid card (Joker)
    print("Testing Invalid Card:")
    try:
        card1 = Card(suite="Joker", rank="A")
        card1.printCard()
    except TypeError as e:
        print(f"Successfully caught error: {e}")