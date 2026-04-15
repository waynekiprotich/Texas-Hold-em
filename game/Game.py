from Deck import Deck
from Player import Player

class Game():
    def __init__(self):
        self.pot = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
        
        # Initial Deal (2 cards each)
        human_cards = [self.deck.give_card(), self.deck.give_card()]
        pc_cards = [self.deck.give_card(), self.deck.give_card()]
        
        self.human = Player(type="human", cards=human_cards, bet=0, name="John", amount=2000)
        self.pc = Player(type="pc", cards=pc_cards, bet=0, name="Stockfish", amount=2000)
        
        self._turn = self.human
        self.community_cards = []

    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, player):
        if isinstance(player, Player):
            self._turn = player
        else:
            raise ValueError("The turn must be assigned to a player object")

    # --- Game Flow Methods ---

    def deal_community(self, number):
        """Deals a specified number of cards to the table (Flop, Turn, River)."""
        for _ in range(number):
            self.community_cards.append(self.deck.give_card())

    def gather_bets(self):
        """Collects bets into the main pot."""
        self.pot += self.human.bet + self.pc.bet
        self.human.bet = 0
        self.pc.bet = 0

    def print_community_card(self):
        print("Community cards:")
        for card in self.community_cards:
            card.print_card()

    # --- Helper Methods for Sorting (Bubble Sort) ---

    def get_card_value(self, card):
        """Converts face cards to numbers so the computer knows Jack > 10."""
        if card.rank == "J": return 11
        if card.rank == "Q": return 12
        if card.rank == "K": return 13
        if card.rank == "A": return 14
        return int(card.rank)

    def sort_cards(self, cards):
        """Uses the Bubble Sort algorithm to order cards from lowest to highest."""
        n = len(cards)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare the numerical values of adjacent cards
                val1 = self.get_card_value(cards[j])
                val2 = self.get_card_value(cards[j + 1])
                
                # Swap them if the left card is bigger than the right card
                if val1 > val2:
                    cards[j], cards[j + 1] = cards[j + 1], cards[j]
        return cards

    # --- Winning Hand Logic ---

    def check_royal_flush(self, player):
        """Checks for 10, J, Q, K, A of the same suit."""
        all_cards = player.cards + self.community_cards
        royal_ranks = ["10", "J", "Q", "K", "A"]
        
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            matches = [c for c in all_cards if c.suite == suit and c.rank in royal_ranks]
            if len(matches) == 5:
                return True
        return False

    def check_straight_flush(self, player):
        """Checks for 5 consecutive cards of the SAME suit."""
        all_cards = player.cards + self.community_cards
        
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            # 1. Isolate cards of the current suit
            suited_cards = [c for c in all_cards if c.suite == suit]
            
            # 2. We need at least 5 suited cards to even attempt a straight flush
            if len(suited_cards) >= 5:
                
                # 3. Sort those suited cards using Bubble Sort
                sorted_suited = self.sort_cards(suited_cards)
                
                # 4. Count consecutive cards
                consecutive_count = 1
                for i in range(len(sorted_suited) - 1):
                    current_val = self.get_card_value(sorted_suited[i])
                    next_val = self.get_card_value(sorted_suited[i + 1])
                    
                    if next_val == current_val + 1:
                        consecutive_count += 1
                        if consecutive_count == 5:
                            return True  # Found 5 in a row!
                    elif next_val != current_val:
                        # Gap found, reset the counter back to 1
                        consecutive_count = 1
                        
        return False

# --- Testing the Engine ---
if __name__ == "__main__":
    game = Game()
    
    print("--- Texas Hold'em Engine Initialized ---")
    
    # Simulate a full hand being dealt to the table
    game.deal_community(3) # Flop
    game.deal_community(1) # Turn
    game.deal_community(1) # River
    
    print("\nSimulating Checks on John's hand...")
    print(f"Has Royal Flush: {game.check_royal_flush(game.human)}")
    print(f"Has Straight Flush: {game.check_straight_flush(game.human)}")