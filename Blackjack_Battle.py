import random
import sys
def blackJack(state):
    state.gprint("""
He questions you on what you are doing in his office until he notices the answer key in your hand.
You attempt to run but the door slams shut and you cannot pry in open. You turn
around and Dr. Buck has a deck of cards on his deck and asks if you want to play.
He challanges you to a game of blackjack.
---hint---
This game of blackjack is a version where each hand determines who and how much damage is dealt. Your goal is to reduce Dr. Buck's health from 50 to zero before he does the same to your 65 health. Winning a hand deals damage to Dr. Buck based on the difference in card values, while losing means you take the damage. Strategically decide when to hit or stand, and avoid busting to ensure your survival!
----------
    """)
    #Intial Health Values
    buck_Health = 50
    player_Health = 65
    while buck_Health>0 and player_Health>0:
        state.gprint(f"Your health is {player_Health} and Dr. Buck's health is {buck_Health}")
        #Resets variables for new round
        aces = 0
        aces_comp = 0
        action = ""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        #Pre-action cards
        card1 = deck.pop()
        card2 = deck.pop()
        card3 = deck.pop()
        hidden_card4 = deck.pop()
        hand_val_player = card_values[card1[0]] + card_values[card3[0]]
        hand_val_computer = card_values[card2[0]]
        if card1[0]=='Ace':
            aces+=1
        if card2[0]=='Ace':
            aces_comp +=1
        if card3[0]=='Ace':
            aces+=1
        if hidden_card4[0]=='Ace':
            aces_comp+=1
        #Fixes edge case
        if aces == 2:
            hand_val_player -=10
            aces -=1
        #Informs player of cards
        state.gprint(f"Your first two cards are {card1[0]} of {card1[1]} and {card3[0]} of {card3[1]} for a total of {hand_val_player}.")
        state.gprint(f"Dr. Buck's first card is the {card2[0]} of {card2[1]}.")

        while True:
            if hand_val_player<=21:
                    action = input("Do you want to hit or stand? ").strip().lower()
                    if action =="hit":
                        drawcard = deck.pop()
                        hand_val_player += card_values[drawcard[0]]
                        if drawcard[0] == 'Ace':
                            aces+=1
                        if hand_val_player>21 and aces>0:
                            aces-=1
                            hand_val_player-=10
                        state.gprint(f"You drew the {drawcard[0]} of {drawcard[1]} and your new hand value is {hand_val_player}.")
                    elif action == "stand":
                        state.gprint(f"You stand with {hand_val_player}.")
                        break
                    else:
                        print(f"Dr. Buck does not understand {action} and requests that you say hit or stand.")
                        
            else:
                state.gprint("You have busted. Your hand is now worth 0")
                hand_val_player = 0
                break
        hand_val_computer += card_values[hidden_card4[0]]
        state.gprint(f"Dr. Buck flips over his hidden card and it is the {hidden_card4[0]} of {hidden_card4[1]} and their new total is {hand_val_computer}.")
        while hand_val_computer <= 21:
            if hand_val_computer <= 17:
                drawcard = deck.pop()
                hand_val_computer += card_values[drawcard[0]]          
                if drawcard[0] == 'Ace':
                    aces_comp += 1
                if hand_val_computer > 21 and aces_comp > 0:
                    aces_comp -= 1
                    hand_val_computer -= 10
                state.gprint(f"Dr. Buck draws the {drawcard[0]} of {drawcard[1]}. Their new total is {hand_val_computer}.")
            else:
                state.gprint(f"Dr. Buck stands with {hand_val_computer}.")
                break
        if hand_val_computer > 21:
            buck_Health= buck_Health - hand_val_player
            state.gprint(f"Dr. Buck busted. You deal {hand_val_player} to him.")
        elif hand_val_player > hand_val_computer:
            damage_Buck = hand_val_player-hand_val_computer
            buck_Health = buck_Health - damage_Buck
            state.gprint(f"You deal {damage_Buck} to Dr. Buck.")
        elif hand_val_computer > hand_val_player:
            damage_player = hand_val_computer - hand_val_player
            player_Health = player_Health - damage_player
            state.gprint(f"Dr. Buck deals {damage_player} to you.")
        else: 
            state.gprint("Your hand values were the same neither person deals any damage.")
    if buck_Health<=0:
        state.gprint("""
You have defeated Dr. Buck in a game of blackjack. He 
looks at you with dread and allows you to leave the room
answer key in hand. You succesfully pass the final exam 
and are able to move on with your college journey.
              """)
        print("--------------------")
        state.gprint("Thank you for playing!!!")
        sys.exit
    elif player_Health<=0:
        state.gprint("""
Dr. Buck defeats you in his card game and rips the answer key
out of your hand. He stands up and tightly grabs your arm as he
escorts you down the hall. You pass numerous students who point
and laugh at you before arriving at the office of student conduct.
You are told your time at UMD has come to an end. You have been expelled.
              """)
        print("--------------------")
        state.gprint("Aw shucks better luck next time.")
        sys.exit
       
