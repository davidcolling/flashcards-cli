A python script that prints data to the console from specially-formatted (yet simple) files incrementally for use as flashcards for all your spaced-repition needs.

The file format rules:
    - The "front of the card" comes first. It can fill at most one line of text. This line does not contain a whitespace character in the first column (at the start).
    - The "back of the card" comes on the lines preceding its respective "front of the card". It can fill multiple lines in the file. Each line must start with a space;

A demonstration cards file:

======================

front of the card

    back of the card
    back of the card
    back of the card


front of the card

    back of the card
    back of the card

front of the card

    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card
    back of the card

======================


remember to
export DOCKER = <path to directory containing this directory>

