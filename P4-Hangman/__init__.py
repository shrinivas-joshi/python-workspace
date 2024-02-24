import images
import words_list
import random
from replit import clear

print(images.logo)

# Choose random word from the word list
random_word = random.choice(words_list.word_list)
hidden_word = []

# Creating a list with blanks, len is that of the random word
for _ in range(len(random_word)):
    hidden_word.append('_')

# Instantiating the number of chances the player has.
chances = len(images.stages)-1


game_is_running = True
while game_is_running:
    user_ans = input('Guess One Letter: ').lower()
    clear()
    if user_ans in hidden_word:
        print(f"You have already guessed the word: {user_ans}")
    for position in range(len(random_word)):
        if user_ans == random_word[position]:
            hidden_word[position] = user_ans
    print(f"{''.join(hidden_word)}")
    if user_ans not in random_word or len(user_ans) == 0:
        print(f"You guessed {user_ans}, that's not in the word. You lose a life.")
        print(images.stages[chances])
        chances -= 1

    if chances == -1:
        print("You Have Lost.")
        print(f"The Answer was {random_word}")
        game_is_running = False;
    elif '_' not in hidden_word and chances != 0:
        game_is_running = False
        print('You Have WONNNNNN!!!!!!')


