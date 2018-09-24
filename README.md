# bulls_and_cows
Bulls and Cows guessing game written in python using pygame

This is a number guessing game where the player has to guess a 4 digit random number where no digit has the same number. The goal of the player is to guess the right number within 10 guesses.

After each guess, the player is given feedback on howclose there guess is to the real number. If the a guess shares a digit with the actual number, then this is counted as a hit. If the guess shares a number with the actual number but not a
digit, then it is counted as a blow.

For example:

actual number = 1234

guess = 1743

In this case, the guess has 1 hit and 2 blows

## Installation and Dependencies
Run `python main.py` to play the game. Also, pygame is needed for to run this game. This can be done most easily with the pip tool and can usually be run with the follow command:

`pip install pygame` 

If problems stil occur then check that python is up to date.
