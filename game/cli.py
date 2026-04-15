'''
dealing cards
handling betting rounds
revealing community cards 
deciding the winner.
'''
from Game import Game

def play_game():
    game=Game()

    # to initialize players
    human=game.human
    pc=game.pc

    # person to start
    game.turn=human
    
    # Initial bets 
    human_amount=human.place_initial_bet()
    human.bet=human_amount
    
    #PC play
    pc_amount=pc.auto_match_or_raise(human_amount)
    pc.bet=pc_amount

    # to ckeck fold 
    if pc_amount=="l":
        print("Towel thrown in. Human won.")
        return
    
    game.turn=human

    k = 0

    # Betting round 1
    print("-------------------")
    print("Starting 1st betting round")
    print("---------------------")
    while True:
        print("Round ",k)
        print("------------------\n")
        if k>=1 and pc.bet==human.bet:
            print("All bets are equal. End the betting round")
            break
        k=k+1

        # human play
        human_choice=human.call_fold_raise(player=pc)
        #fold check human
        if human_choice=="l":
            print("PC WON THE GAME")
            return
        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        # PC play
        pc_choice=pc.auto_call_raise(player=human,k=k)
        # fold check pc
        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")

    print("-------------------")
    print("Completed 1st betting round")
    print("---------------------")
    
    # Deal Flop
    deck=game.deck
    deck.burn_card() # removes top card
    # to show the 3 community cards
    game.community_cards.append(deck.give_card())
    game.community_cards.append(deck.give_card())
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("--------------------")
    
    # all the money is added
    game.pot = game.pot + human.bet + pc.bet
    #reset bet for both
    human.reset_bet()
    pc.reset_bet()

    print("All money moved to betting pot")
    print("POT AMOUNT ",game.pot)
    print("--------------------")

    # Betting round 2
    print("-------------------")
    print("Starting 2nd betting round")
    print("---------------------")

    k=0
    while True:
        if k>0 and pc.bet==human.bet:
            print("All bets are equal. End the betting round")
            break
        k=k+1

        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return
        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")

    print("-------------------")
    print("Completed 2nd betting round")
    print("---------------------")
    
    # Deal Turn
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("--------------------")
    
    game.pot = game.pot + human.bet + pc.bet
    human.reset_bet()
    pc.reset_bet()
    print("All money moved to betting pot")
    print("POT AMOUNT ",game.pot)
    print("--------------------")

    # betting round 3
    print("-------------------")
    print("Starting 3rd betting round")
    print("---------------------")

    k=0
    while True:
        if k>0 and pc.bet==human.bet:
            print("All bets are equal. End the betting round")
            break
        k=k+1

        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return
        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")

    print("-------------------")
    print("Completed 3rd betting round")
    print("---------------------")
    
    # Deal River
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("--------------------")
    
    game.pot = game.pot + human.bet + pc.bet
    human.reset_bet()
    pc.reset_bet()
    print("All money moved to betting pot")
    print("POT AMOUNT ",game.pot)
    print("--------------------")

    print("-------------------")
    print("Starting Final betting round")
    print("---------------------")

    k=0
    while True:
        if k>0 and pc.bet==human.bet:
            print("All bets are equal. End the betting round")
            break
        k=k+1

        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return
        
        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc amount",pc.amount)
        print("pc bet amount",pc.bet)
        print("-----------------------")
        
    game.pot = game.pot + human.bet + pc.bet
    human.reset_bet()
    pc.reset_bet()

    # Showdown
    print("\n===========================")
    print("        SHOWDOWN!          ")
    print("===========================")
    print(f"FINAL POT: ${game.pot}")

    print("\n--- Player's Hand ---")
    for card in human.cards:
        card.print_card()

    print("\n--- PC's Hand ---")
    for card in pc.cards:
        card.print_card()

    print("\n--- Community Cards ---")
    game.print_community_card()
    print("---------------------------\n")

    #check who won 
    if game.check_royal_flush(human):
        print("Player wins with a Royal Flush.")
        human.amount += game.pot
    elif game.check_royal_flush(pc):
        print("PC wins with a Royal Flush.")
        pc.amount += game.pot

    elif game.check_straight_flush(human):
        print("Player wins with a Straight Flush.")
        human.amount += game.pot
    elif game.check_straight_flush(pc):
        print("PC wins with a Straight Flush.")
        pc.amount += game.pot

    elif game.check_four_of_a_kind(human):
        print("Player wins with Four of a Kind.")
        human.amount += game.pot
    elif game.check_four_of_a_kind(pc):
        print("PC wins with Four of a Kind.")
        pc.amount += game.pot

    elif game.check_full_house(human):
        print("Player wins with a Full House.")
        human.amount += game.pot
    elif game.check_full_house(pc):
        print("PC wins with a Full House.")
        pc.amount += game.pot

    elif game.check_flush(human):
        print("Player wins with a Flush.")
        human.amount += game.pot
    elif game.check_flush(pc):
        print("PC wins with a Flush.")
        pc.amount += game.pot

    elif game.check_straight(human):
        print("Player wins with a Straight.")
        human.amount += game.pot
    elif game.check_straight(pc):
        print("PC wins with a Straight.")
        pc.amount += game.pot

    elif game.check_three_of_a_kind(human):
        print("Player wins with Three of a Kind.")
        human.amount += game.pot
    elif game.check_three_of_a_kind(pc):
        print("PC wins with Three of a Kind.")
        pc.amount += game.pot

    elif game.check_two_pair(human):
        print("Player wins with Two Pair.")
        human.amount += game.pot
    elif game.check_two_pair(pc):
        print("PC wins with Two Pair.")
        pc.amount += game.pot

    elif game.check_pair(human):
        print("Player wins with a Pair.")
        human.amount += game.pot
    elif game.check_pair(pc):
        print("PC wins with a Pair.")
        pc.amount += game.pot

    else:
        print("Nobody has a pair. Checking High Card...")
        human_high = max([game.get_card_value(card) for card in human.cards])
        pc_high = max([game.get_card_value(card) for card in pc.cards])

        if human_high > pc_high:
            print("Player wins with High Card.")
            human.amount += game.pot
        elif pc_high > human_high:
            print("PC wins with High Card.")
            pc.amount += game.pot
        else:
            print("It's a Tie. Split Pot.")
            human.amount += game.pot // 2
            pc.amount += game.pot // 2

if __name__ == "__main__":
    play_game()