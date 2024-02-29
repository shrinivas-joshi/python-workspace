from logo import logo
from replit import clear

total_bids = {}


def add_bid(person, value):
    total_bids[person] = value


def winning_bid():
    highest_bid = 0
    winner = ""
    for bidder in total_bids:
        if total_bids[bidder] > highest_bid:
            highest_bid = total_bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of Rs.{highest_bid}")


print(logo)
print('Welcome to the secret auction program.')

take_more_bids = 'yes'
while take_more_bids == 'yes':
    name = input("What is your name?:").capitalize()
    amount = int(input("What's your bid?:Rs. "))
    add_bid(name, amount)
    take_more_bids = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if take_more_bids == 'yes':
        clear()
    else:
         winning_bid()

