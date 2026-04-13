from game.Game import Game

def run_betting_round(game, round_name):
   
    human = game.human
    pc = game.pc
    
    print(f"\n--- {round_name.upper()} BETTING ---")
    
     
    current_highest_bet = max(human.total_amount_bet, pc.total_amount_bet)
    turns_taken = 0

    while True:
        if turns_taken >= 1 and human.total_amount_bet == pc.total_amount_bet:
            print(f"Betting round finished. Total Pot: {game.pot}")
            return True
        
        turns_taken += 1

        human_action = human.call_fold_raise(player_obj=pc)
        
        if human_action == "l": # Human Folded
            print(f"\nYou folded. {pc.name} takes the pot of {game.pot}.")
            return False
        
        human.update_amount_bet(human_action)

        if isinstance(human_action, int) and human.total_amount_bet > current_highest_bet:
            current_highest_bet = human.total_amount_bet

        pc_action = pc.auto_match_or_raise(current_highest_bet)
        
        if pc_action == "l": # PC Folded
            print(f"\n{pc.name} folded! You win the pot of {game.pot}!")
            return False
        
        pc.update_amount_bet(pc_action)
 
        if isinstance(pc_action, int) and pc.total_amount_bet > current_highest_bet:
            current_highest_bet = pc.total_amount_bet

        game.pot = human.total_amount_bet + pc.total_amount_bet
        print(f"Current Pot: {game.pot}")


def play_game():
    # Initialize the engine 
    game = Game()
    
    print("Welcome to Texas Hold'em CLI!")
    print(f"Your starting balance: {game.human.amount}")
    

    game.deal_hole_cards()
    print("\n[YOUR HAND]")
    for card in game.human.cards:
        card.printCard()

    if not run_betting_round(game, "Pre-Flop"):
        return 

    print("\n>>> DEALING THE FLOP (3 Cards)")
    game.deal_community(3)
    game.show_table() 
    
    if not run_betting_round(game, "The Flop"):
        return

    print("\n>>> DEALING THE TURN (1 Card)")
    game.deal_community(1)
    game.show_table()
    
    if not run_betting_round(game, "The Turn"):
        return

    print("\n>>> DEALING THE RIVER (1 Card)")
    game.deal_community(1)
    game.show_table()
    
    if not run_betting_round(game, "The River"):
        return

    print("\n--- SHOWDOWN ---")
    print(f"{game.pc.name}'s hidden cards were:")
    for card in game.pc.cards:
        card.printCard()


    human_highest_card = max(c.value for c in game.human.cards)
    pc_highest_card = max(c.value for c in game.pc.cards)

    if human_highest_card > pc_highest_card:
        print(f"\nCongratulations! You win the pot of {game.pot} chips!")
    elif pc_highest_card > human_highest_card:
        print(f"\nPC wins the pot of {game.pot} chips. Better luck next time!")
    else:
        print(f"\nIt's a draw! Splitting the pot of {game.pot}.")

if __name__ == "__main__":
    play_game()