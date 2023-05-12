import string
import random

"""
    Password Picker will enable you to create strong passwords by
    combining words, numbers, and characters. When you run the program,
    it will create a new password and show it on the screen. 
    You can ask it to keep creating new passwords until you find one you like. 
"""
# Easy To Remember Hard To Crack

print('Welcome Come To Password Picker !!')

adjectives = [
    'sleepy', 'slow', 'wet', 'fat', 'white', 'green', 'fluffy',
    'fast', 'smelly', 'proud', 'brave', 'red', 'orange'
]

nouns = [
    'apple', 'mango', 'dinosaur', 'goat', 'lion',
    'man', 'ball', 'duck', 'panda'
]
while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    number = random.randrange(0,100)

    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char

    print(f'Your Password : {password}')

    next_step = input('Would You Like Another Password? Type Y or N').lower()

    if next_step=='n':
        break