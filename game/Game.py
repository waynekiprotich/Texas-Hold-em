from Deck import Deck
from Player import Player

class Game():

    def __init__(self):
        self.pot = 0
        # Total money in the middle of the table

        self.community_cards = [] 
        # Cards shared by all players (flop/turn/river in poker)

        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
        # Creates and shuffles deck twice (extra shuffle, not required but fine)

        # Deal 2 cards to human player
        human_cards = [self.deck.give_card(), self.deck.give_card()]
        
        # Deal 2 cards to computer player
        pc_cards = [self.deck.give_card(), self.deck.give_card()]
        
        self.human = Player(type="human", cards=human_cards, bet=0, name="John", amount=2000)
        # Human player with starting chips and hole cards

        self.pc = Player(type="pc", cards=pc_cards, bet=0, name="Stockfish", amount=2000)
        # Computer player with same setup

        self._turn = self.human
        # Tracks whose turn it is (starts with human)
    
    @property
    def turn(self):
        # Allows safe access to current player turn
        return self._turn
    
    @turn.setter
    def turn(self, player):
        # Controls who can be assigned as turn
        if isinstance(player, Player):
            self._turn = player
        else:
            raise ValueError("The turn must be assigned to a Player object")
        # Prevents invalid assignment (only Player objects allowed)

    def gather_bets(self):
        """
        Collects bets from both players into the main pot
        and resets their individual bet values for next round
        """
        self.pot += self.human.bet + self.pc.bet
        # Add both players' bets into pot

        self.human.bet = 0  
        self.pc.bet = 0     
        # Reset bets after collecting

        print(f"Bets gathered. The main pot is now ${self.pot}")
        # Show updated pot
        
if __name__ == "__main__":
    game = Game()
    print(f"Game initialized. Starting pot: ${game.pot}")
    # Creates a new game instance

    print("\n--- PC Cards ---")
    game.pc.cards[0].printCard()
    game.pc.cards[1].printCard()
    # Shows computer's hole cards

    print("\n--- Human Cards ---")
    game.human.cards[0].printCard()
    game.human.cards[1].printCard()
    # Shows human player's hole cards