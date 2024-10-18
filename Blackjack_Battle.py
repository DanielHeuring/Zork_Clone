import random

def blackJack():
    global wins, buck_Health, player_Health, stay
    print("""
You here rattles coming from the dark corner of his office. All of the sudden
a dark figure emerges. You scream out in terror. "AHhhhhh" You realize it was 
Dr. Buck and are a little embaressed that you screamed. He questions you on
what you are doing in his office until he notices the answer key in your hand.
You attempt to run but the door slams shut and you cannot pry in open. You turn
around and Dr. Buck has a deck of cards on his deck and asks if you want to play.
He wants to play a version of blackjack where the difference in value damages your health. 
    """)
    buck_Health = 50
    player_Health = 65
    while buck_Health>0 and player_Health>0:
        print(f"Your health is {player_Health} and Dr. Buck's health is {buck_Health}")
        aces = 0
        aces_comp = 0
        stay = ""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
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

        print(f"Your first two cards are {card1[0]} of {card1[1]} and {card3[0]} of {card3[1]} for a total of {hand_val_player}.")
        print(f"The dealers card is the {card2[0]} of {card2[1]}.")

        while True:
            if hand_val_player<=21:
                    stay = input("Do you want to hit or stand? ").strip().lower()
                    if stay =="hit":
                        drawcard = deck.pop()
                        hand_val_player += card_values[drawcard[0]]
                        if drawcard[0] == 'Ace':
                            aces+=1
                        if hand_val_player>21 and aces>0:
                            aces-=1
                            hand_val_player-=10
                        print(f"You drew the {drawcard[0]} of {drawcard[1]} and your new hand value is {hand_val_player}.")
                    elif stay == "stand":
                        print(f"You stand with {hand_val_player}.")
                        break
                    else:
                        print(f"Dr. Buck does not understand {stay} and requests that you say hit or stand.")
                        
            else:
                print("You have busted. Your hand is now worth 0")
                hand_val_player = 0
                break
        hand_val_computer += card_values[hidden_card4[0]]
        print(f"The dealer flips over his hidden card and it is the {hidden_card4[0]} of {hidden_card4[1]} and their new total is {hand_val_computer}.")
        while hand_val_computer <= 21:
            if hand_val_computer <= 17:
                drawcard = deck.pop()
                hand_val_computer += card_values[drawcard[0]]          
                if drawcard[0] == 'Ace':
                    aces_comp += 1
                if hand_val_computer > 21 and aces_comp > 0:
                    aces_comp -= 1
                    hand_val_computer -= 10
                print(f"The dealer draws the {drawcard[0]} of {drawcard[1]}. Their new total is {hand_val_computer}.")
            else:
                print(f"The dealer stands with {hand_val_computer}.")
                break
        if hand_val_computer > 21:
            buck_Health= buck_Health - hand_val_player
            print(f"Dr. Buck busted. You deal {hand_val_player} to him.")
        elif hand_val_player > hand_val_computer:
            damage_Buck = hand_val_player-hand_val_computer
            buck_Health = buck_Health - damage_Buck
            print(f"You deal {damage_Buck} to Dr. Buck.")
        elif hand_val_computer > hand_val_player:
            damage_player = hand_val_computer - hand_val_player
            player_Health = player_Health - damage_player
            print(f"Dr. Buck deals {damage_player} to you.")
        else: 
            print("Your hand values were the same neither person deals any damage.")
    if buck_Health<=0:
        print("""
You have defeated Dr. Buck in a game of blackjack. He 
looks at you with dread and allows you to leave the room
answer key in hand. You succesfully pass the final exam 
and are able to move on with your college journey.
              """)
    elif player_Health<=0:
        print("""
Dr. Buck defeats you in his card game and rips the answer key
out of your hand. He stands up and tightly grabs your arm as he
escorts you down the hall. You pass numerous students who point
and laugh at you before arriving at the office of student conduct.
You are told your time at UMD has come to an end. You have been expelled.
              """)
blackJack()
