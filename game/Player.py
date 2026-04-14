import random   
import time     

class Player():

    def __init__(self, type="pc", cards=[], bet=0, name="", amount=0):
        # initializes a player (PC or human)
        self.name = name
        self.type = type
        self.cards = cards
        self._bet = bet   # internal bet tracking
        self.amount = amount  # player money

    @property
    def bet(self):
        # returns current bet value
        return self._bet
        
    @bet.setter
    def bet(self, amount):
        # updates bet and reduces player money
        self._bet = self._bet + amount
        self.amount = self.amount - amount

    def place_initial_bet(self):
        # asks player to place starting bet with validation
        while True:
            amount = input(f"Place initial bet amount. Current amount is {self.amount}: ")

            if amount.isdigit():
                n = int(amount)
                if n > 0 and n <= self.amount:
                    self.bet = n
                    return n
                
                print("Invalid amount entered.")
                print(f"Amount must range from 1 to {self.amount}")
                print("Try again")
            else:
                print(f"Enter a number as valid amount between 1 and {self.amount}")

    def call_fold_raise(self, player):
        # main decision menu: call, fold, or raise
        choice = input("Press 1 to call \nPress 2 to fold \nPress 3 to raise: ")
        if choice == '1':
            return self.call(player)
        if choice == '2':
            return self.fold(player)
        if choice == '3':
            return self.raise_stake(player)
            
        print(f"Wrong choice {choice}. Choose 1 to 3")
        return self.call_fold_raise(player)
    
    def call(self, player):
        # match current bet
        print("Amount Bet is ", player.amount)
        diff = self.bet - player.bet

        if diff > 0:
            return True
            
        diff = abs(diff)
        if self.amount > diff:
            print("Cant call, not enough money")
            return "l"
            
        self.bet = diff
        print(f"I call your bet.\nI bet ${diff}")

    def fold(self, player):
        # player gives up round
        print('I Fold')
        return "l"
    
    def raise_stake(self, player):
        # increase bet amount
        raise_amount = input(f"Enter raise amount. Max amount {self.amount}: ")
        raise_amount = int(raise_amount)
        if raise_amount > self.amount:
            print("Check and restart process")
            return self.raise_stake(player)
            
        print(f"I raise by amount ", raise_amount)
        self.bet = raise_amount
        return raise_amount

    def auto_match_or_raise(self, amount):
        # comp logic for pc player decision making
        print("Pc thinking. What to do...")
        time.sleep(2)  # delay for realism
        to_do = random.randint(1, 2)  # randomly choose action
        raise_amount = amount + random.randint(10, 250) 

        if raise_amount > self.amount:
            to_do = 1  # force call if cannot raise

        if to_do == 1:
            if self.amount > amount:
                self.bet = amount
                print(f"Matching your action. Bet {amount}")
                return amount
            else:
                return "l"
        
        self.bet = raise_amount
        print("I have a good feeling. I raise by ", raise_amount)
        return raise_amount