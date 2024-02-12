import random
import logos

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
choices = [logos.rock, logos.paper, logos.scissors]

user_choice = choices[user_input]

computer_choice = choices[random.randint(0, len(choices) - 1)]

print(user_choice)
print("Computer Chose:")
print(computer_choice)

if user_choice == computer_choice:
    print("DRAW")
elif ((user_choice == choices[0] and computer_choice == choices[2]) or
      (user_choice == choices[1] and computer_choice == choices[0]) or
      (user_choice == choices[2] and computer_choice == choices[1])):
    print("You Win !!!!")
else:
    print("Computer Wins :( :( :(")
