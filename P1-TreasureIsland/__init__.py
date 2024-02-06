import logofile

print(logofile.logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

user_decision = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n=> ").lower()
if user_decision != 'left':
    print("Unlucky :( You fell into the hole. GAME OVER")
else:
    user_decision = input("You have come to a lake. There is an island in the middle of the lake. Type "
                          "\"wait\" to wait for the boat. Type \"swim\" to swim across.\n=> ").lower()
    if user_decision != 'wait':
        print("Unlucky :( You got attacked by an angry trout. GAME OVER")
    else:
        user_decision = input("You have arrived at the island unharmed. there is a house with 3 doors."
                              "One red, One Yellow and One Blue\n=> ").lower()
        if user_decision == 'red':
            print("Unlucky :( Burned by fire. GAME OVER")
        elif user_decision == 'blue':
            print("Unlucky :( Eaten by beasts. GAME OVER")
        elif user_decision == 'yellow':
            print("You WINN")
        else:
            print("Unlucky :( Incorrect Entry. GAME OVER")
