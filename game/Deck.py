from Card import Card
import random

class Deck():
    
    def __init__(self):
        # Creates a full 52-card deck
        ranks = Card.RANKS
        suites = Card.SUITES 
        deck = []

        # Nested loop builds every combination of rank + suit
        for rank in ranks:
            for suite in suites:
                card = Card(suite=suite, rank=rank)
                deck.append(card)

        self.deck = deck
        # Stores deck in the object


    def shuffle(self):
        newDeck = []
        deck = self.deck

        # Manually shuffles by randomly picking cards out of the deck
        while True:
            if len(deck) == 1:
                card = deck[0]
                newDeck.append(card)
                break
            
            n = random.randint(0, len(deck) - 1)
            
            card = deck[n]
            deck.pop(n)
            newDeck.append(card)
            
        self.deck = newDeck
        # Replaces old deck with shuffled version


    def burn_card(self):
        # Moves top card to bottom 
        if len(self.deck) > 0:
            top_card = self.deck.pop() 
            self.deck.insert(0, top_card) 


    def give_card(self):
        # Deals a card from the top of the deck
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            print("No cards left in deck!")
            return None



if __name__ == "__main__":
    d1 = Deck()
    d1.shuffle()
    # Creates and shuffles a deck for testing