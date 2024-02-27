from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(user_message, shift_number, direction):
    new_message = ''
    if direction == 'decode':
        shift_number *= -1
    for letter in user_message:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_message += alphabet[current_index + shift_number]
        else:
            new_message += letter
    return new_message


next_round = True

while next_round:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type Your Message:\n").lower()
    shift = int(input("Type The Shift Number:\n"))
    if shift > 26:
        shift = shift % 26
    print(f"Here's the decoded result: {caesar(message, shift, action)}")
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again != 'yes':
        next_round = False
