class Card():
    # This class represents a card in the game
    RANKS=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    SUITES=["HEART","DIAMOND","SPADE","CLUBS"]
    #
    def __init__(self,suite,rank):


        if not isinstance(suite,str):
            raise TypeError(f"Suite expected to be a string got {type(suite).__name__}")

        if not isinstance(rank,str):
            raise TypeError(f"Suite expected to be a string got {type(rank).__name__}")

        suiteUpper=suite.upper()
        rankUpper=rank.upper()
        if rankUpper in Card.RANKS:
            pass
        else:
            raise TypeError(f"Added rank not in rank list {acceptedRanks}")

        if suiteUpper in Card.SUITES:
            pass
        else:
            raise TypeError(f"Added suite not in suite list {acceptedSuits}")

        self.rank=rankUpper
        self.suite=suiteUpper

    def printCard(self):
        print("Rank",self.rank)
        print("Suite",self.suite)

if __name__=="__main__":
    card1=Card(suite="Joker",rank="A")
    card1.printCard()

    card2=Card(suite="Clubs",rank="3")
    card2.printCard()