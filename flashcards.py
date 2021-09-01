import re
flashcards = open('../cpbox/cards.txt', 'r')
lines = flashcards.readlines()
for line in lines:
    if re.match(r'\s', line):
        print(line)
    else:
        input()
        print(line)
        input()
