from art import (logo, vs)
import random
from data import data
import replit


def checkHighCount(follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return 'A'
    else:
        return 'B'


user_is_wrong = False
first_option = random.choice(data)
score = 0
print(logo)
while not user_is_wrong:
    if score != 0:
        print(f"You're right! Current Score is {score}")
    print(f"Compare A: {first_option['name']},a {first_option['description']}, from {first_option['country']}")
    print(vs)
    second_option = random.choice(data)
    print(f"Compare B: {second_option['name']},a {second_option['description']}, from {second_option['country']}")

    user_value = input("Who has more followers? Type 'A' or 'B': ").upper()

    expected_result = checkHighCount(first_option['follower_count'], second_option['follower_count'])

    if user_value != expected_result:
        user_is_wrong = True
        print(f"Sorry that's wrong. Final Score: {score}")
    else:
        score += 1
        replit.clear()
