from Deck import Deck
from Player import Player

class Game():

    def __init__(self):
        self.pot=0
        deck=Deck()
        deck.shuffle()
        deck.shuffle()
        
        human_cards= [deck.give_card(),deck.give_card()]
        pc_card=[deck.give_card(),deck.give_card()]
        
        self.human=Player(type="human", cards=human_cards, bet=0, name="John", amount=2000)
        self.pc=Player(type="pc", cards=pc_card, bet=0, name="Stockfish", amount=2000)
        
        self._turn=self.human
        self.deck=deck
        self.community_cards=[]
    
    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self,player):
        if isinstance(player,Player):
            self._turn=player
        else:
            raise ValueError("The turn must be assigned to a player object")

    def print_community_card(self):
        print("Community cards")
        for card in self.community_cards:
            card.print_card()

    def get_card_value(self, card):
        if card.rank == "J": return 11
        if card.rank == "Q": return 12
        if card.rank == "K": return 13
        if card.rank == "A": return 14
        return int(card.rank)

    def sort_cards(self, cards):
        n = len(cards)
        for i in range(n):
            for j in range(0, n - i - 1):
                val1 = self.get_card_value(cards[j])
                val2 = self.get_card_value(cards[j + 1])
                if val1 > val2:
                    cards[j], cards[j + 1] = cards[j + 1], cards[j]
        return cards

    def get_rank_counts(self, cards):
        counts = {}
        for card in cards:
            val = self.get_card_value(card)
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        return counts

    def check_royal_flush(self, player):
        all_cards = player.cards + self.community_cards
        royal_ranks = ["10", "J", "Q", "K", "A"]
        
        for suit in ["HEART", "DIAMOND", "CLUBS", "SPADE"]:
            matches = [c for c in all_cards if c.suite == suit and c.rank in royal_ranks]
            if len(matches) == 5:
                return True
        return False

    def check_straight_flush(self, player):
        all_cards = player.cards + self.community_cards
        
        for suit in ["HEART", "DIAMOND", "CLUBS", "SPADE"]:
            suited_cards = [c for c in all_cards if c.suite == suit]
            if len(suited_cards) >= 5:
                sorted_suited = self.sort_cards(suited_cards)
                consecutive_count = 1
                for i in range(len(sorted_suited) - 1):
                    current_val = self.get_card_value(sorted_suited[i])
                    next_val = self.get_card_value(sorted_suited[i + 1])
                    if next_val == current_val + 1:
                        consecutive_count += 1
                        if consecutive_count == 5:
                            return True
                    elif next_val != current_val:
                        consecutive_count = 1
        return False

    def check_four_of_a_kind(self, player):
        all_cards = player.cards + self.community_cards
        counts = self.get_rank_counts(all_cards)
        for val, count in counts.items():
            if count >= 4:
                return True
        return False

    def check_full_house(self, player):
        all_cards = player.cards + self.community_cards
        counts = self.get_rank_counts(all_cards)
        has_three = False
        has_two = False
        for val, count in counts.items():
            if count >= 3:
                has_three = True
            elif count >= 2:
                has_two = True
        return has_three and has_two

    def check_flush(self, player):
        all_cards = player.cards + self.community_cards
        suit_counts = {"HEART": 0, "DIAMOND": 0, "CLUBS": 0, "SPADE": 0}
        for card in all_cards:
            suit_counts[card.suite] += 1
        for count in suit_counts.values():
            if count >= 5:
                return True
        return False

    def check_straight(self, player):
        all_cards = player.cards + self.community_cards
        unique_vals = []
        for card in all_cards:
            val = self.get_card_value(card)
            if val not in unique_vals:
                unique_vals.append(val)
                
        n = len(unique_vals)
        for i in range(n):
            for j in range(0, n - i - 1):
                if unique_vals[j] > unique_vals[j + 1]:
                    unique_vals[j], unique_vals[j + 1] = unique_vals[j + 1], unique_vals[j]
                    
        consecutive_count = 1
        for i in range(len(unique_vals) - 1):
            if unique_vals[i + 1] == unique_vals[i] + 1:
                consecutive_count += 1
                if consecutive_count >= 5:
                    return True
            else:
                consecutive_count = 1
        return False

    def check_three_of_a_kind(self, player):
        all_cards = player.cards + self.community_cards
        counts = self.get_rank_counts(all_cards)
        for val, count in counts.items():
            if count >= 3:
                return True
        return False

    def check_two_pair(self, player):
        all_cards = player.cards + self.community_cards
        counts = self.get_rank_counts(all_cards)
        pair_count = 0
        for val, count in counts.items():
            if count >= 2:
                pair_count += 1
        return pair_count >= 2

    def check_pair(self, player):
        all_cards = player.cards + self.community_cards
        counts = self.get_rank_counts(all_cards)
        for val, count in counts.items():
            if count >= 2:
                return True
        return False