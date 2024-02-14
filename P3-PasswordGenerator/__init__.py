import random
import database

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordstr = []

for num in range(1, nr_letters + 1):
    passwordstr.append(random.choice(database.letters))

for num in range(1, nr_symbols + 1):
    passwordstr.append(random.choice(database.symbols))

for num in range(1, nr_numbers + 1):
    passwordstr.append(random.choice(database.numbers))

random.shuffle(passwordstr)

print(''.join(passwordstr))
