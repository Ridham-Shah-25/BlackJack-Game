logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

user_question = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n':")
while (user_question == 'y'):
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    user_cards = [card1, card2]
    current_score = card1 + card2
    card3 = random.choice(cards)
    computer_cards = [card3]
    computer_score = card3
    print("Your cards: {}".format(user_cards) + "current_score:" +
          str(current_score))
    print("Computer's first card:" + str(card3))
    user_input = input("Type 'y' to get another card, type 'n' to pass")
    while (user_input == 'y'):
        card4 = random.choice(cards)
        user_cards.append(card4)
        current_score += card4
        print("Your cards: {}".format(user_cards) + "current_score:" +
              str(current_score))
        print("Computer's first card:" + str(card3))
        if (current_score > 21):
            break
        user_input = input("Type 'y' to get another card, type 'n' to pass")
    print("Your final hand: {}".format(user_cards) + ",Final score:" +
          str(current_score))
    while (computer_score < 17):
        card5 = random.choice(cards)
        computer_cards.append(card5)
        computer_score += card5
    print("Computer's final hand: {}".format(computer_cards) +
          ",Final score:" + str(computer_score))
    if (current_score > 21):
        print("You went over.you Lose")
    elif (computer_score > 21):
        print("Opponent went over. You win")
    elif (current_score > computer_score):
        print("You win")
    elif (current_score == computer_score):
        print("Draw")
    else:
        print("You lose")
    user_question = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':")
    from replit import clear
    clear()
