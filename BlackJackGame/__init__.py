from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# deal_card() function that uses the List below to *return* a random card 11 is the Ace.
def deal_card():
    return random.choice(cards)


# calculate_score() that takes a List of cards as input and returns the score.
def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) >= 21:
        card_list.remove(11)
        card_list.insert(1)
    return sum(card_list)


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 0:
        return "User Loses. Computer Got A BLACKJACK"
    elif user_score == 0:
        return "Computer Loses. You Got A BLACKJACK"
    elif user_score > 21:
        return "You went over, Computer Wins"
    elif computer_score > 21:
        return "Computer went over, You Win"
    elif user_score > computer_score:
        return "You Win. Computer Loses."
    else:
        return "You Lose. Computer Wins"


def play_game():
    computer_score = 0
    user_score = 0
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_is_on = True
    while game_is_on:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        if comp_score == 0 or user_score == 0 or user_score > 21:
            game_is_on = False
        else:
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_again == 'y':
                user_cards.append(deal_card())
            else:
                game_is_on = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Deck: {user_cards}")
    print(f"Computer Final Deck: {computer_cards}")
    print(f"{compare(user_score,computer_score)}")


while input("Do you want to play Blackjack? Enter 'y' or 'n': ") == "y":
    clear()
    play_game()
