import re

number_of_cards = 0
score = 0

flashcards = open('../cpbox/cards.txt', 'r')
lines = flashcards.readlines()
for line in lines:
    if re.match(r'\s', line):
        print(line)
    else:
        if (number_of_cards != 0) :
            this_score = input("Enter points to add: ")
            score += int(this_score)
        print(line)
        number_of_cards += 1
        input()

this_score = input("Enter points to add: ")
score += int(this_score)

print(str(score) + " / " + str(number_of_cards))
