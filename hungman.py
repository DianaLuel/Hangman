import random

from art import logo
print(logo)

from art import word_list

chosen_word = random.choice(word_list)
# # Check
# print(chosen_word)

lives = 6
empty = []

for i in chosen_word:
    empty.append('_')

from art import stages

def update_empty(let):
        place = chosen_word.find(let)
        empty[place] = let

# letters = []
# def enter_letter():

#     letter_entered_correctly = False

#     while not letter_entered_correctly:

#         lett = input("Enter a letter: ")

#         letters.append(lett)
        
#         if lett in letters:
#             print(f"You already entered letter {lett}, enter another letter.")
#         else:
#             letter_entered_correctly = True
#             return lett


def enter_letter():

    letter_entered_correctly = False

    while not letter_entered_correctly:

        lett = input("Enter a letter: ").lower

        if lett in empty:
            print(f"You already entered letter {lett}, enter another letter.")
        else:
            letter_entered_correctly = True
            return lett

end_of_game = False

print(f"You have {lives} to start with.")
print(empty)
print(stages[lives])
while not end_of_game:

    letter = enter_letter()

    if letter in chosen_word:
        print(f"Letter {letter} is found in the word.")
        update_empty(letter)
        print(empty)
        print(stages[lives])
        if '_' not in empty:
            print("The game is ove, You win:(")
            end_of_game = True

    else:
        print(f"Letter {letter} doesn't found in the word.")
        lives-=1
        print(empty)
        print(stages[lives])
        print(f"You have {lives} lives left.")
        if lives < 1:
            print("Game Over!\nYou lose:(")
            end_of_game = True