"""
Forces valid card values only.
Converts input to uppercase.
Prevents invalid cards, e.g., 'joker'
Stores rank + suit in an object
Print card details
"""

class Card:

    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITES = ["HEART", "DIAMOND", "SPADE", "CLUBS"]

    def __init__(self, suite, rank):

        if not isinstance(suite, str):
            raise TypeError(f"Suite expected string, got {type(suite).__name__}")

        if not isinstance(rank, str):
            raise TypeError(f"Rank expected string, got {type(rank).__name__}")

        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        if rankUpper not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rankUpper}")

        if suiteUpper not in Card.SUITES:
            raise ValueError(f"Invalid suite: {suiteUpper}")

        self.rank = rankUpper
        self.suite = suiteUpper

    def print_card(self):
        print(f"{self.rank} {self.suite}")
        print("-" * 15)


if __name__ == "__main__":

    print("Testing Valid Card:")
    card2 = Card(suite="SPADE", rank="5")
    card2.print_card()

    print("Testing Invalid Card:")
    try:
        card1 = Card(suite="Joker", rank="A")
        card1.print_card()
    except ValueError as e:
        print(f"Successfully caught error: {e}")