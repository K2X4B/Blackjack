#___________________________Eenentwintig_Version:11.0_Win_stable.py____________________2025-01-28______#
import random
import time

# Set player's starting ammount of chips (20 chips = 10 plays, 2 chips are bet per game)
bank = 20

# The main/outer loop
game_loop = True
while game_loop:

    # Start the game
    play = input("Would you like to play (y/n)?   ")
    if play == "y":
        game_finished = False

        # End the game when the player os out of chips
        if bank <= 0:
            print("You have no more chips to play with.")
            print("Game Over!")
            bank = 20
            print("Restarting the game. One moment...")
            time.sleep(2)
            game_finished = True

        # Game setup...
        # List of possible cards that can be drawn from the deck
        # The House aka your score to beat (one of their cards is hidden from the player)
        # Generate two random cards and append them to the dealer's hand
        # Added deck_h so the dealer can't draw a 1
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        deck_h = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # Set vale of Ace
        A = 11

        # The House
        house_hand = []
        house_score = 0
        house_bust = False
        house_bj = False

        # The House's hand. The dealer will continue to draw cards until they have <= 17 or go bust
        while house_score < 17:
            house_draw = (random.choice(deck_h))
            house_hand.append(house_draw)
            house_score = sum(house_hand)

        # To track if the House is bust
        if house_score > 21:
            house_bust = True

        # Check House for Blackjack
        if house_hand[0] == 1 and house_hand[1] == 10:
            house_bj = True
            house_hand[0] = A
        if house_hand[0] == 10 and house_hand[1] == 1:
            house_bj = True
            house_hand[1] = A

        # The player
        player_hand = []
        player_bust = False
        new_card = 0
        player_score = 0
        player_bj = False

        # Player's starting hand
        new_card = (random.choice(deck))
        player_hand.append(new_card)
        new_card = (random.choice(deck))
        player_hand.append(new_card)

        # Check player for Blackjack
        if player_hand[0] == 1 and player_hand[1] == 10:
            player_bj = True
            player_hand = [A, 10]
        if player_hand[0] == 10 and player_hand[1] == 1:
            player_bj = True
            player_hand = [10, A]
            
        # Main game play
        while not game_finished:

            #  and print current info
            print("------------------------------------------------------------------------")
            print("Bank: ", end=" ")
            print(bank, end=" ")
            print(" chips")
            print("The House is showing a ", end=" ")
            print(house_draw)
            print("Your hand: ", end=" ")
            print(player_hand)
            
            # Drawing cards
            hit = input("Would you like a card (y/n)?     ")
            print("------------------------------------------------------------------------")
            if hit == "y":
                # Generate a new card and print it
                # Append the new card to the player's hand and print their hand
                new_card = (random.choice(deck))
                print("You were dealt a ", end=" ")
                print(new_card)
                player_hand.append(new_card)
                player_score = sum(player_hand)
                print("Your hand: ", end=" ")
                print(player_hand)

                # Check to see if the player is bust
                player_score = sum(player_hand)
                if player_score > 21:
                    b2 = True
                    print("Bust!")
                    bank = bank - 2
                    player_bust = True
                    game_finished = True

            # When the player stays
            elif hit == "n":

                # Solve for the Aces
                player_score = sum(player_hand)
                if 1 in player_hand and player_score < 12:
                    player_hand.append(10) # Note: This will add an extra card (10) to the players hand to show the ace being used as an 11
                else:
                    ace = False
                player_score = sum(player_hand)

                # Show the results
                print("Okay, let's see how you did...")
                print("Your hand: ", end=" ")
                print(player_hand, end=" ")
                print(player_score)
                house_score = sum(house_hand)
                print("Dealer's hand: ", end=" ")
                print(house_hand, end=" ")
                print(house_score)
                push = False
                if player_bj == True and house_bj == True:
                    push = True
                if player_score == house_score:
                    push = True
                if player_bj == True:
                    print("Blackjack!")
                
                # End the hand/round
                play = False

                # Check to see who won
                house_score = sum(house_hand)
                player_score = sum(player_hand)
                # Tie aka push
                if push == True:
                    print("Push")
                    game_finished = True
                # Player Bust
                elif player_bust == True:
                    print("Player Bust! The House wins.")
                    bank = bank - 2
                    game_finished = True             
                # House Bust
                elif house_bust == True and player_bust == False:
                    print("The dealer is bust. Congratulations, you win!")
                    bank = bank + 3
                    game_finished = True
                # House wins
                elif player_score < house_score:
                    print("The house wins. Better luck next time")
                    bank = bank - 2
                    game_finished = True
                # Player wins
                else: 
                    print("Congratulations! You won.")
                    bank = bank + 3
                    game_finished = True

            # In case of PEBKAC
            else:
                print("Please answer y or n.")
                game_finished = False

    # Exiting the game, roll credits            
    elif play == "n":
        print("Thank you for Playing!")
        print("credits:")
        print("Mattchu Pichu = Creative Lead - Coder - Play Tester")
        print("Meilindis = Coder - Debugger - Play Tester")
        print("Queen Mergh = Play Tester - Researcher - Wheezle Wrangler")
        print("Eloise = Emotional Support Sausage - Wheezle")
        print("Special thaks to 17th century Spain and or Fance for inventing the game; Vingt-Un")
        print("The program will end in a few second. Good Bye!")
        time.sleep(4)
        print("KTB")
        time.sleep(0.5)
        game_loop = False
    # Error message if player enters something other than y/n    
    else:
        print("Please answer y or n.")

# Credits:

    # -=[Mattchu Pichu]=- 
                            # Creative Lead - Coder - Play Tester
    # -=[Meilindis]=- 
                            # Coder - Debugger - Play Tester
    # -=[Queen Mergh]=-
                            # Play Tester - Researcher - Wheezle Wrangler
    # -=[Eloise]=-
                            # Emotional Support Sausage - Wheezle
    
    # Special thaks to 17th century Spain (and/or Fance) for inventing the game; Vingt-Un.

















































































































































































































# ------------------------------ The Dopefish Lives ------------------------#

#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW..;;;;;.WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWW.;;;;;;;WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWWW;;;;;;;;;WWWWWWWWWWWWWWWWWWWWWW..WWWWWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWW.;;;;;;;;.WWWWWWWWWWWWWWWWWWWWWWW..;;.WWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWW...;;;.......;;..WWWWWWWWWWWWWWWWWWWWWWWW.;;..WWWWWWWWW
#WWWWWWWWWWWWWWWW...;;;;;;;;;;;;;;;;;;;;;;..WWWWWWWWWWWWWWWWWWWW.;;;.WWWWWWWW
#WWWWWWWWWWWWWW.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWWWWWWWWWWWWWWW.;;;;..WWWWWW
#WWWWWWWWWWW;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.WWWWWWWWWWWWWW.;;;;;..WWWWW
#WWWWWWWWW.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.WWWWWWWWWWWW.;;;;;;..WWWW
#WWWWWWW....;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.WWWWWWWWWW.;;;;;;;;..WWW
#WWWWW.WWW..WWWWV..;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+..WWWWWWW.;;;;;;;;;..WWW
#WWW.WWWWWWWWWWWWWWWW;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWW.;;;;;;;;;;;..WWW
#WW.VW......WWWWWWWWW.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;....;;;;;;;;;;;..WWWW
#WW.WW......WWWWWWWWWW.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWWW
#WW..WWW.....WWWWWWWWV.;;;;;;...;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWWWWWW
#WW.;.W.WWWWWWWWWWWWW.;;;;;;;;..;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.WWWWWWWW
#WW...;.VW..WWWWWWWW.;..;;;;;;..;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWWWW
#WWW......;;;......;;;;;;..;;;..;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWWW
#WWW.WW.VV...............;;;;;..;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;..WWWW
#WWW.WW.WWWWV.;;;;;;.;....;;;...;;;;;;;;;;;;;;;;;;;;;;;;....;;;;;;;;;;;..WWWW
#WWW.WW.WWWWV....;;;;;;;..;;;..;;;;;;;;;;;;;;;;;;;;;;;..WWWW..;;;;;;;;;..WWWW
#WWW.WW.WWWWV.;;;;;;.;;;;.;;;;;;;;;;;;;;;;;;;;;..;;....WWWWWW..;;;;;;;;..WWWW
#WWW.WW.WWWWV.....;;;;;;;;;;;;;;;;;;;;;;;;;.;;;;....WWWWWWWWWWW.;;;;;;..WWWWW
#WWW.WW.WWWWV.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.;;.....WWWWWWWWWWWW.;;;;;;..WWWWW
#WWW....WWWWV..;;;;;;;.;;;;;;;;;;;;;;;;;;;;......WWWWWWWWWWWWWW.;;;;;..WWWWWW
#WWWWWWW...WV.WW......+;;;;;;;;;;;;;;;;;;;;;...WWWWWWWWWWWWWWW.;;;;;;.WWWWWWW
#WWWWWWWWWWWWWWWWWWWWW..;;;;;;;;;;;;;;;;;...WWWWWWWWWWWWWWWWWW.;;;..WWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWW..;;;;;;;;;...WWWWWWWWWWWWWWWWWWWWWW.;;.WWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
# Image Credit: <https://cc314.shikadi.net/oldcc314/ascii-dopefish.htm>     #